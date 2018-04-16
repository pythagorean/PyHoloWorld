	(function () {
		var __name__ = '__main__';
		var xmlHttpRequest = function () {
			return new XMLHttpRequest ();
		};
		var holoWorldEntryCreate = function (task, callback) {
			var xhr = xmlHttpRequest ();
			var url = '/fn/HoloWorld/holoWorldEntryCreate';
			xhr.open ('POST', url, true);
			xhr.setRequestHeader ('Content-type', 'application/json');
			var onreadystatechange = function () {
				if (xhr.readyState == 4 && xhr.status == 200) {
					callback (JSON.parse (xhr.responseText));
				}
			};
			xhr.onreadystatechange = onreadystatechange;
			var data = JSON.stringify (dict ({'content': task, 'timestamp': 101010}));
			xhr.send (data);
		};
		var holoWorldEntryRead = function (hash, callback) {
			var xhr = xmlHttpRequest ();
			var url = '/fn/HoloWorld/holoWorldEntryRead';
			xhr.open ('POST', url, true);
			xhr.setRequestHeader ('Content-type', 'application/json');
			var onreadystatechange = function () {
				if (xhr.readyState == 4 && xhr.status == 200) {
					callback (JSON.parse (xhr.responseText));
				}
			};
			xhr.onreadystatechange = onreadystatechange;
			var data = JSON.stringify (hash);
			xhr.send (data);
		};
		var submitEntry = function () {
			event.preventDefault ();
			var holoWorldEntry = document.getElementById ('holoWorldEntry').value;
			var callback = function (hash) {
				document.getElementById ('hash').value = hash;
			};
			holoWorldEntryCreate (holoWorldEntry, callback);
		};
		var readEntry = function () {
			event.preventDefault ();
			var hash = document.getElementById ('hash').value;
			var callback = function (task) {
				document.getElementById ('entryContent').value = task.content;
			};
			holoWorldEntryRead (hash, callback);
		};
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.holoWorldEntryCreate = holoWorldEntryCreate;
			__all__.holoWorldEntryRead = holoWorldEntryRead;
			__all__.readEntry = readEntry;
			__all__.submitEntry = submitEntry;
			__all__.xmlHttpRequest = xmlHttpRequest;
		__pragma__ ('</all>')
	}) ();
