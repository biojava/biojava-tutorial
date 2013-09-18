BioJava 3 tutorial
=================

A brief introduction into BioJava 3.

== 

The goal of this tutorial is to provide an educational introduction into some of the features that are provided by BioJava. 

At the moment this tutorial is still under development. Please check  the [BioJava Cookbook](http://biojava.org/wiki/BioJava:CookBook3.0) for a more comprehensive collection of many examples of what is possible with BioJava and how to do things.

## Index

Book 1: [The Protein Structure modules](structure/README.md)


<script type="text/javascript" src="JSmol.min.js"></script>

<script type="text/javascript">

// 1/21/2013 10:54:15 PM -- adds image handling

var jmolApplet0; // set up in HTML table, below

// logic is set by indicating order of USE -- default is HTML5 for this test page, though
var use = "HTML5" // JAVA HTML5 WEBGL IMAGE  are all otions
var s = document.location.search;


// Developers: The debugCode flag is checked in j2s/core/core.z.js, 
// and, if TRUE, skips loading the core methods, forcing those
// to be read from their individual directories. Set this
// true if you want to do some code debugging by inserting
// System.out.println, document.title, or alert commands
// anywhere in the Java or Jmol code.

Jmol.debugCode = (s.indexOf("debugcode") >= 0);

jmol_isReady = function(applet) {
    Jmol._getElement(applet, "appletdiv").style.border="1px solid blue"
}       

var xxxx = document.location.search
if (xxxx.length == 5 || xxxx.length == 0) {
    xxxx = (xxxx + "?1crn").substring(1,5)
    script = 'h2oOn=true;set animframecallback "jmolscript:if (!selectionHalos) {select model=_modelNumber}";'
    +'set errorCallback "myCallback";'
    +'set defaultloadscript "isDssp = false;set defaultVDW babel;if(!h2oOn){display !water}";'
    +'set zoomlarge false;set echo top left;echo loading XXXX...;refresh;'
    +'load "http://www.rcsb.org/pdb/files/XXXX.pdb";set echo top center;echo XXXX;'
    +'spacefill off;wireframe off;cartoons on;color structure;'
    script = script.replace(/XXXX/g, xxxx)
} else {
    script = unescape(xxxx.substring(1))
}


var Info = {
    width: 450,
    height: 450,
    debug: false,
    color: "white",
    addSelectionOptions: false,
    serverURL: "http://chemapps.stolaf.edu/jmol/jsmol/php/jsmol.php",
    use: "HTML5",
    j2sPath: "j2s",
    readyFunction: jmol_isReady,
    script: script,
    //jarPath: "java",
    //jarFile: (useSignedApplet ? "JmolAppletSigned.jar" : "JmolApplet.jar"),
    //isSigned: useSignedApplet,
    //disableJ2SLoadMonitor: true,
    disableInitialConsole: true
    //defaultModel: "$dopamine",
    //console: "none", // default will be jmolApplet0_infodiv
}

</script>


<script type="text/javascript">

jmolApplet0 = Jmol.getApplet("jmolApplet0", Info)

</script>
