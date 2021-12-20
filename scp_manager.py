import paramiko
import scp


class SCPManager:
    def __init__(self, hostname=None, username=None, password=None, port=None):
        self.ssh_client = None
        self.credentials = dict(hostname=hostname, username=username, password=password, port=port)
        
    def open(self, **kwargs):
        if self.ssh_client is not None:
            self.close()
        self.credentials.update(kwargs)
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(**self.credentials)
        self.credentials = {}
        return self
        
    def close(self):
        if self.ssh_client is not None:
            self.ssh_client.close()
            self.ssh_client = None
            
    def _build_scp_client(self):
        if self.ssh_client is not None:
            return scp.SCPClient(self.ssh_client.get_transport())
        raise ValueError("Not connected")

    def put(self, local_path, remote_path, recursive=False, preserve_times=True, **kwargs):
        with self._build_scp_client() as client:
            client.put(local_path, remote_path, recursive=recursive, preserve_times=preserve_times, **kwargs)

    def get(self, remote_path, local_path, recursive=False, **kwargs):
        with self._build_scp_client() as client:
            client.get(remote_path, local_path, recursive=recursive, **kwargs)

    def single_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.readlines()
    
    def __enter__(self):
        return self.open()
    
    def __exit__(self, exception, exc_type, traceback):
        self.close()
