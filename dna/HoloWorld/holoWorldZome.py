__pragma__ ('noalias', 'get') # Defaults to py_get, js_get to get

def holoWorldEntryCreate(entry):
    return commit('holoWorldEntry', entry)

def holoWorldEntryRead(hash):
    return js_get(hash)

def genesis():
    return True

def validateCommit(entryName, entry, header, pkg, sources):
    if entryName == 'holoWorldEntry': return True
    else: return False

def validatePut(entryName, entry, header, pkg, sources):
    if entryName == 'holoWorldEntry': return True
    else: return False

def validateMod(entryName, entry, header, replaces, pkg, sources):
    if entryName == 'sampleEntry': return True
    else: return False

def validateDel(entryName, hash, pkg, sources):
    if entryName == 'sampleEntry': return True
    else: return False

def validateLink(linkEntryType, baseHash, links, pkg, sources):
    return False

def validatePutPkg(entryName):
    return None

def validateModPkg(entryName):
    return None

def validateDelPkg(entryName):
    return None

def validateLinkPkg(entryName):
    return None
