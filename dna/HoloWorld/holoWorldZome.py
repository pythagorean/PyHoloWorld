# EXPOSED METHODS

# creates a holoWorldEntry entry
def holoWorldEntryCreate(entry):
    return hc_commit('holoWorldEntry', entry)

# retrieves a holoWorldEntry entry
def holoWorldEntryRead(hash):
    return hc_get(hash)

 # Called only when your source chain is generated
 # return {boolean} success
def genesis():
    return True

#-----------------------------------------------------------------
# validation functions for every DHT entry change
#-----------------------------------------------------------------

def validateCommit(entryName, entry, header, pkg, sources):
    if entryName == 'holoWorldEntry':
        # in order for the 'commit' action to work, validateCommit (given a holoWorldEntry) must return True
        # there is no special validation that we have to perform for our simple app
        return True
    # default: invalid entry name
    return False

def validatePut(entryName, entry, header, pkg, sources):
    if entryName == 'holoWorldEntry':
        return True
    # default: invalid entry name
    return False

def validatePutPkg(entryName):
    return None
