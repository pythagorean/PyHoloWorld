def xmlHttpRequest(): return __new__ (XMLHttpRequest())

def holoWorldEntryCreate(task, callback):
    xhr = xmlHttpRequest()
    url = '/fn/HoloWorld/holoWorldEntryCreate'
    xhr.open('POST', url, True)
    xhr.setRequestHeader('Content-type', 'application/json')
    def onreadystatechange():
        if xhr.readyState == 4 and xhr.status == 200:
            callback(JSON.parse(xhr.responseText))
    xhr.onreadystatechange = onreadystatechange
    data = JSON.stringify({'content': task, 'timestamp': 101010})
    xhr.send(data)

def holoWorldEntryRead(hash, callback):
    xhr = xmlHttpRequest()
    url = '/fn/HoloWorld/holoWorldEntryRead'
    xhr.open('POST', url, True)
    xhr.setRequestHeader('Content-type', 'application/json')
    def onreadystatechange():
        if xhr.readyState == 4 and xhr.status == 200:
            callback(JSON.parse(xhr.responseText))
    xhr.onreadystatechange = onreadystatechange
    data = JSON.stringify(hash)
    xhr.send(data)

def submitEntry():
    event.preventDefault()
    holoWorldEntry = document.getElementById('holoWorldEntry').value
    def callback(hash): document.getElementById('hash').value = hash
    holoWorldEntryCreate(holoWorldEntry, callback)

def readEntry():
    event.preventDefault()
    hash = document.getElementById('hash').value
    def callback(task): document.getElementById('entryContent').value = task.content
    holoWorldEntryRead(hash, callback)
