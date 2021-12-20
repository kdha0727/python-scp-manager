# Python SCP Manager

Enhanced scp-wrapper python module that enables continuous operations

---

# How to use

## As context manager

```python

from scp_manager import SCPManager

# Enter your remote credentials
with SCPManager(hostname='127.0.0.1', username='dhakim', password='kdha0727', port=22) as wrapper:

    # From remote to local
    wrapper.get(
        local_path='path/to/local/destination', 
        remote_path='path/to/remote/source', 
        recursive=False,  # True when handling folder
    )
    
    # From local to remote
    wrapper.put(
        local_path='path/to/remote/destination', 
        remote_path='path/to/local/source', 
        recursive=False,  # True when handling folder
    )

```

## When connecting lazily

```python

from scp_manager import SCPManager

wrapper = SCPManager()

# Some your operations
...

try:

    # Connect: Enter your remote credentials
    wrapper.open(hostname='127.0.0.1', username='dhakim', password='kdha0727', port=22)

    # From remote to local
    wrapper.get(
        local_path='path/to/local/destination', 
        remote_path='path/to/remote/source', 
        recursive=False,  # True when handling folder
    )

    # From local to remote
    wrapper.put(
        local_path='path/to/remote/destination', 
        remote_path='path/to/local/source', 
        recursive=False,  # True when handling folder
    )

finally:
    
    # You are required to close manager when operations are done
    wrapper.close()

```

or

```python

from scp_manager import SCPManager

wrapper = SCPManager()

# Some your operations
...

# Connect: Enter your remote credentials
with wrapper.open(hostname='127.0.0.1', username='dhakim', password='kdha0727', port=22):

    # From remote to local
    wrapper.get(
        local_path='path/to/local/destination', 
        remote_path='path/to/remote/source', 
        recursive=False,  # True when handling folder
    )

    # From local to remote
    wrapper.put(
        local_path='path/to/remote/destination', 
        remote_path='path/to/local/source', 
        recursive=False,  # True when handling folder
    )

```

---
