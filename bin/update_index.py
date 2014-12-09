#!/usr/bin/env python
"""
This script generates the footers for all markdown files. Rerun the script
after adding new books or chapters in order to update the footer sections on
each page with links to the next and previous chapters.

The script works by recursively parsing "## Index" sections in files, starting
with README.md. The footer is marked with an HTML comment, `automatically
generated footer`.  Any text after this comment is destroyed by the script, so
all edits should be made above that point.

"""

import sys,os,re

class TutorialIndex(object):

    footermark = u"<!--automatically generated footer-->"

    def __init__(self,link,chapter=None,title=None,parent=None):
        """Create a new TutorialIndex

        :param link:    A link to this page, relative to parent's link
        :param chapter: The chapter number, e.g. "Chapter 5"
        :param title:   The chapter title, e.g. "Writing Docstrings"
        :param parent:  The TutorialIndex which references this one
        """
        self.link = link
        self.chapter = chapter
        self.title = title
        self.parent = parent
        self.children = []

    def parse(self):
        """Parse the index, add a footer, and do the same for each child
        found in the '# Index' section (if any).

        Caution, this method overwrites any existing footer sections on this
        file and all children!
        """

        #Recognise and parse "<CHAPTER>: (<TITLE>)[<LINK>]"
        indexentry = re.compile("^(.*)[:-].*\[([^]]*)\]\(([^)]*)\).*$")

        filename = self.rootlink()

        with open(filename,"r+") as file:
            line = file.readline()
            had_footer=False

            # Parse file for index, truncate prior footer, and append footermark
            in_index = False
            while line:
                if line[0] == u"#": #That's a header, not a comment
                    if u"index" in line.lower():
                        in_index = True
                    else:
                        in_index = False
                elif line.strip() == TutorialIndex.footermark: # Footer already!
                    had_footer=True
                    file.truncate()
                    break
                elif in_index:
                    # look for 'Chapter 1: [Title](link)'
                    result = indexentry.match(line)
                    if result:
                        chapter,title,link = result.groups()
                        child = TutorialIndex(link,chapter,title,self)
                        self.children.append(child)

                line = file.readline()

            # Append footer
            if not had_footer:
                file.write(u"\n")
                file.write(TutorialIndex.footermark)
                file.write(u"\n")
            footer = self.makefooter()
            file.write(footer)

        # Recurse to children
        for child in self.children:
            child.parse()

    def rootlink(self):
        """Convert self.link to an absolute path relative to the root TutorialIndex
        :return: The path to this TutorialIndex relative to the root index
        """
        if self.parent is None:
            return self.link
        parentlink = self.parent.rootlink()

        return os.path.join(os.path.dirname(parentlink),self.link)

    def makefooter(self):
        """ makefooter() -> str

        Creates the footer text (everything below the "automatically generated
        footer" line)
        """
        # Don't include footer on main page
        if self.parent is None:
            return ""

        lines = ["","---","","Navigation:"]
        # Iterate over parents
        p = self.parent
        linkmd = [self.makename()] #reverse order (self to root)
        while p is not None:
            name = p.makename()
            # Get a path to p relative to our own path
            link = os.path.relpath(p.rootlink(),os.path.dirname(self.rootlink()))
            linkmd.append("[{}]({})".format(name,link))
            p = p.parent
        linkmd.reverse()
        lines.append("\n| ".join(linkmd))

        lines.append("")

        if self.parent is not None:
            pos = self.parent.children.index(self) #Should always work
            if pos > 0:
                prev = self.parent.children[pos-1]
                name = prev.makename()
                link = os.path.relpath(prev.rootlink(),os.path.dirname(self.rootlink()))
                lines.append("Prev: [{}]({})".format(name,link))
                lines.append("")
            if pos < len(self.parent.children)-1:
                next = self.parent.children[pos+1]
                name = next.makename()
                link = os.path.relpath(next.rootlink(),os.path.dirname(self.rootlink()))
                lines.append("Next: [{}]({})".format(name,link))
                lines.append("")

        #lines.append(self.makename()+", "+self.link)
        return "\n".join(lines)

    def makename(self):
        """ Return a name, like "<CHAPTER>: <TITLE>"
        """
        if self.chapter:
            name = self.chapter
            if self.title:
                name += ": " + self.title
        elif self.title:
            name = self.title
        else:
            name = self.link #last resort

        return name

    def __repr__(self):
        return "TutorialIndex({self.link!r},{self.chapter!r},{self.title!r},{parent!r})" \
                .format(self=self,parent=self.parent.title if self.parent else None)

if __name__ == "__main__":
    # Set root index
    root = TutorialIndex("README.md",title="Home")

    # Rewrite headers
    root.parse()

    # Output tree
    def pr(node,indent=""):
        print "{}{}".format(indent,node.link,node.rootlink())
        for n in node.children:
            pr(n,indent+"  ")

    pr(root)
