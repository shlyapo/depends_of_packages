import apt_pkg
import sys

# from gettext import gettext as _
import gettext


#def _(s): return gettext.dgettext("python-apt", s)


class BaseDependency(object):
    def __init__(self, name, rel, ver, pre):
        self.name = name
        self.relation = rel
        self.version = ver
        self.preDepend = pre


class Dependency(object):
    def __init__(self, alternatives):
        self.or_dependencies = alternatives


class Package(object):
    depends_list = []
    def __init__(self, cache, depcache, records, name, pcache):
        """ Init the Package object """
        #self._cache = cache  # low level cache
        #self._depcache = depcache
        #self._records = records
        self._name = name
        #self._pkg = pkgiter
        #self._list = sourcelist  # sourcelist
        #self._pcache = pcache  # python cache in cache.py
        pass

    def getDependencies(self):
        depends = ver.DependsList
        for t in ["PreDepends", "Depends"]:
            if not depends.has_key(t):
                continue
            for depVerList in depends[t]:
                base_deps = []
                for depOr in depVerList:
                    base_deps.append(
                        BaseDependency(depOr.TargetPkg.Name, depOr.CompType, depOr.TargetVer, (t == "PreDepends")))
                depends_list.append(Dependency(base_deps))
        return depends_list


    def sourcePackageName(self):
        """ Return the source package name as string """
        if not self._lookupRecord():
            if not self._lookupRecord(UseCandidate=False):
                return self._pkg.Name
        src = self._records.SourcePkg
        if src != "":
            return src
        else:
            return self._pkg.Name

    sourcePackageName = property(sourcePackageName)

    def homepage(self):
        """ Return the homepage field as string """
        if not self._lookupRecord():
            return None
        return self._records.Homepage

    homepage = property(homepage)


if __name__ == "__main__":

    apt_pkg.init()
    cache = apt_pkg.GetCache()
    depcache = apt_pkg.GetDepCache(cache)
    records = apt_pkg.GetPkgRecords(cache)
    sourcelist = apt_pkg.GetPkgSourceList()

    pkgiter = cache["apt-utils"]
    pkg = Package(cache, depcache, records, sourcelist, None, pkgiter)

    "Dependencies: %s" % pkg.installedDependencies
    for dep in pkg.candidateDependencies:
        print
        ",".join(["%s (%s) (%s) (%s)" % (o.name, o.version, o.relation, o.preDepend) for o in dep.or_dependencies])
    print
    "arch: %s" % pkg.architecture
