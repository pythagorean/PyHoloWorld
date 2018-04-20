__pragma__ ('noalias', 'get') # Defaults to py_get, js_get to get

def holoWorldEntryCreate(entry):
    return commit('holoWorldEntry', entry)

def holoWorldEntryRead(hash):
    return get(hash)

def genesis():
    return True

def validateCommit(entryName, entry, header, pkg, sources):
    if entryName == 'holoWorldEntry': return True
    return False

def validatePut(entryName, entry, header, pkg, sources):
    if entryName == 'holoWorldEntry': return True
    return False

def validatePutPkg(entryName):
    return None
