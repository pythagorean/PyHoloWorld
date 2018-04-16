	(function () {
		var __name__ = '__main__';
		var holoWorldEntryCreate = function (entry) {
			return commit ('holoWorldEntry', entry);
		};
		var holoWorldEntryRead = function (hash) {
			return get (hash);
		};
		var genesis = function () {
			return true;
		};
		var validateCommit = function (entryName, entry, header, pkg, sources) {
			if (entryName == 'holoWorldEntry') {
				return true;
			}
			else {
				return false;
			}
		};
		var validatePut = function (entryName, entry, header, pkg, sources) {
			if (entryName == 'holoWorldEntry') {
				return true;
			}
			else {
				return false;
			}
		};
		var validateMod = function (entryName, entry, header, replaces, pkg, sources) {
			if (entryName == 'sampleEntry') {
				return true;
			}
			else {
				return false;
			}
		};
		var validateDel = function (entryName, hash, pkg, sources) {
			if (entryName == 'sampleEntry') {
				return true;
			}
			else {
				return false;
			}
		};
		var validateLink = function (linkEntryType, baseHash, links, pkg, sources) {
			return false;
		};
		var validatePutPkg = function (entryName) {
			return null;
		};
		var validateModPkg = function (entryName) {
			return null;
		};
		var validateDelPkg = function (entryName) {
			return null;
		};
		var validateLinkPkg = function (entryName) {
			return null;
		};
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.genesis = genesis;
			__all__.holoWorldEntryCreate = holoWorldEntryCreate;
			__all__.holoWorldEntryRead = holoWorldEntryRead;
			__all__.validateCommit = validateCommit;
			__all__.validateDel = validateDel;
			__all__.validateDelPkg = validateDelPkg;
			__all__.validateLink = validateLink;
			__all__.validateLinkPkg = validateLinkPkg;
			__all__.validateMod = validateMod;
			__all__.validateModPkg = validateModPkg;
			__all__.validatePut = validatePut;
			__all__.validatePutPkg = validatePutPkg;
		__pragma__ ('</all>')
	}) ();
