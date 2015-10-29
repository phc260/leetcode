class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):

        degrees = [0]*numCourses
        edges = [[] for i in xrange(numCourses)]
        schedule = []

        for c,p in prerequisites:
            degrees[c] += 1
            edges[p].append(c)

        sources = [i for i in xrange(numCourses) if degrees[i]==0]

        while sources:
            n = sources.pop()
            schedule.append(n)

            for m in edges[n]:
                degrees[m] -= 1
                if degrees[m]==0:
                    sources.append(m)

            while edges[n]:
                edges[n].pop()

        for e in edges:
            if e: return []
        return schedule
