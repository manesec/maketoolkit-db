# SFK Command Example

# Send File or Get Files

## Using FTP

```bash
# [Server]
sfk ftpserv -rw
sfk ftpserv -rw -port=9999

# [Client]
## Uploading a file.
sfk ftp <server_ip>:<port> put <file>

## Zip and upload a file
sfk198.exe zip output.zip <folder_path> -yes

```

## Using Simple File Transfer
Will be Similarity ftp.
```bash
# [Server]
sfk sftserv -rw

# [Client]
sfk sft 192.168.31.158 put <file>
```

## Using Web Server like (simple web server) 
but allow to upload file on web page with : `sfk httpserv -rw -port=8080`

## Full command

```bash
C:\Users\Mane\Downloads\Backup-sfk-main>sfk198.exe
SFK - The Swiss File Knife Multi Function Tool.
Release 1.9.8 Base/XD Revision 2 of Sep 20 2022.
StahlWorks Technologies, http://stahlworks.com/
Distributed for free under the BSD License, without any warranty.

type "sfk commandname" for help on any of the following.
some commands require to add "-help" for the help text.

   file system
      sfk list       - list directory tree contents.
                       list latest, oldest or biggest files.
                       list directory differences.
                       list zip jar tar gz bz2 contents.
      sfk olist      - list office files in a folder,
                       like .docx .xlsx .ods .odt
      sfk filefind   - find files by filename
      sfk treesize   - show directory size statistics
      sfk copy       - copy directory trees additively
      sfk sync       - mirror tree content with deletion
      sfk rename     - flexible multi file rename
      sfk partcopy   - copy part from a file into another one
      sfk mkdir      - create directory tree
      sfk delete     - delete files and folders
      sfk deltree    - delete whole directory tree
      sfk deblank    - remove blanks in filenames
      sfk space [-h] - tell total and free size of volume
      sfk filetime   - tell times of a file
      sfk touch      - change times of a file
      sfk index      - create index file(s) for fast lookup
      sfk name       - lookup file names using index files
      sfk fixfile    - change bad filenames and file times
      sfk setbytes   - set bytes at offset within a file

   compression
      sfk zip        - create zip file from folder
      sfk zipto      - zip selected file list
      sfk unzip      - list or extract zip file
      sfk checkzip   - verify zip file content

   conversion
      sfk oload      - load office file content as text
      sfk lf-to-crlf - convert from LF to CRLF line endings
      sfk crlf-to-lf - convert from CRLF to LF line endings
      sfk detab      - convert TAB characters to spaces
      sfk entab      - convert groups of spaces to TAB chars
      sfk scantab    - list files containing TAB characters
      sfk split      - split large files into smaller ones
      sfk join       - join small files into a large one
      sfk csvtotab   - convert .csv data to tab separated
      sfk tabtocsv   - convert tab separated to .csv format
      sfk encode     - convert data to base64 or hex format
      sfk decode     - decode base64, hex or url format
      sfk wtoa       - convert wide chars to Ansi
      sfk wtou       - convert wide chars to UTF-8
      sfk utoa       - convert UTF-8 text to Ansi
      sfk hexdump    - create hexdump from a binary file
      sfk hextobin   - convert hex data to binary
      sfk hex        - convert decimal number(s) to hex
      sfk dec        - convert hex number(s) to decimal
      sfk chars      - print chars for a list of codes
      sfk bin-to-src - convert binary to source code
      sfk uuencode   - encode binary files as plain text

   text processing
      sfk filter     - search, filter and replace text data
      sfk ofilter    - filter  text from an office file
      sfk replace    - replace words in binary and text files
      sfk xed        - edit stream text using sfk expressions
      sfk xex        - extract from stream text using expressions
      sfk xreplace   - Plus/XE: replace in files using expressions
      sfk run        - run external command on all files of a folder
      sfk runloop    - run a command n times in a loop
      sfk printloop  - print some text many times
      sfk load       - load file content for further processing
      sfk perline    - run sfk command(s) per input text line
      sfk head       - print first lines of a file
      sfk tail       - print last lines of a file
      sfk snapto     - join many text files into one file
      sfk addhead    - insert string at start of text lines
      sfk addtail    - append string at end of text lines
      sfk joinlines  - join text lines split by email reformatting
      sfk strings    - extract strings from a binary file
      sfk sort       - sort text lines produced by another command
      sfk count      - count text lines, filter identical lines
      sfk difflines  - show text lines differing between files
      sfk linelen    - tell length of string(s)

   search and compare
      sfk xfind      - search in text files using
                       wildcards and simple expressions
      sfk ofind      - search in office files .docx .xlsx .ods
      sfk xfindbin   - search in text and binary files
      sfk xhexfind   - search with hexdump output
      sfk extract    - extract data from text and binary
      sfk find       - search static text, without wildcards
      sfk hexfind    - search static binary data
      sfk md5gento   - create list of md5 checksums over files
      sfk md5check   - verify list of md5 checksums over files
      sfk md5        - calc md5 over a file, compare two files
      sfk pathfind   - search PATH for location of a command
      sfk reflist    - list fuzzy references between files
      sfk deplist    - list fuzzy dependencies between files
      sfk dupfind    - find duplicate files by content

   networking
      sfk httpserv   - run an instant HTTP server.
                       type "sfk httpserv -help" for help.
      sfk ftpserv    - run an instant FTP server
                       type "sfk ftpserv -help" for help.
      sfk ftp        - instant FTP client
      sfk web        - send HTTP request to a server
      sfk wget       - download HTTP file from the web
      sfk tcpdump    - print TCP conversation between programs
      sfk udpdump    - print incoming UDP requests
      sfk udpsend    - send UDP requests
      sfk ip         - tell own machine's IP address(es).
                       type "sfk ip -help" for help.
      sfk netlog     - send text outputs to network,
                       and/or file, and/or terminal
      sfk fromnet -h - receive and print network text
      sfk ping       - ping multiple machines in one go
      sfk pingdiff   - find ip of new devices

   scripting
      sfk help chain - how to combine multiple commands
      sfk batch      - run many sfk commands in a script file
      sfk label      - define starting points within a script
      sfk call       - call a sub function at a label
      sfk echo       - print (coloured) text to terminal
      sfk color      - change text color of terminal
      sfk setvar     - put text into an sfk variable
      sfk storetext  - store text in memory for later use
      sfk alias      - create command from other commands
      sfk mkcd       - create command to reenter directory
      sfk sleep      - delay execution for milliseconds
      sfk pause      - wait for user input
      sfk stop       - stop sfk script execution
      sfk tee        - split command output in two streams
      sfk tofile     - save command output to a file
      sfk toterm     - flush command output to terminal
      sfk for        - repeat commands many times
      sfk loop       - repeat execution of all commands
      sfk cd         - change directory within a script
      sfk getcwd     - print the current working directory
      sfk require    - compare version text
      sfk time [-h]  - print current date and time

   development
      sfk bin-to-src - convert binary data to source code
      sfk make-random-file - create file with random data
      sfk fuzz       - change file at random, for testing
      sfk sample     - print example code for programming
      sfk patch      - change text files through a script
      sfk inst       - instrument c++ with tracing calls

   diverse
      sfk view       - show text output in a GUI tool,
                       for interactive browse and filter
      sfk status     - send colored status to the SFKTray
                       Windows GUI utility for display
      sfk calc       - do a simple instant calculation
      sfk random     - create a random number
      sfk prompt     - ask for user input
      sfk number     - print number in diverse formats
      sfk xmlform    - reformat xml  for easy viewing
      sfk jsonform   - reformat json for easy viewing
      sfk video      - how to edit video files
      sfk toclip     - copy command output to clipboard
      sfk fromclip   - read text from clipboard
      sfk env        - search environment variables
      sfk version    - show version of a binary file
      sfk ascii      - list Ansi codepage characters
      sfk ascii -dos - list OEM  codepage characters
      sfk spell      - phonetic spelling for telephone
      sfk cmd        - print an example command
      sfk ruler      - measure console text width
      sfk license    - print the SFK license text
      sfk update     - check for SFK updates
      sfk data       - create random text and test data

   help by subject
      sfk help office   - how to search in office files
      sfk help select   - how dirs and files are selected in sfk
      sfk help options  - general options reference
      sfk help patterns - wildcards and text patterns within sfk
      sfk help chain    - how to combine (chain) multiple commands
      sfk help var      - how to use sfk variables and parameters
      sfk samp          - example scripts on sfk use and for
                          http web access automation
      sfk help shell    - how to optimize the windows command prompt
      sfk help chars    - about locale specific characters
      sfk help nocase   - about case insensitive search
      sfk help unicode  - about unicode file reading support
      sfk help colors   - how to change result colors
      sfk help compile  - how to compile sfk on any linux system

   first time user?

      type "sfk basic" for very basic informations about
      how to select files, general options, shell preparation,
      complex <>|!&?* character issues and color setup.

   to search ALL help text for a topic:

      type "sfk ask word1"    to search all for word1.
      type "sfk ask w1 w2"    to search all for w1 or w2.
      type "sfk dumphelp"     to print ALL help text.

   +----------------------------------------------------------+
   |               Useful? Buy a new coffee mug!              |
   |                   stahlworks.com/merch                   |
   |----------------------------------------------------------|
   |       Get these addons to boost your daily work:         |
   |----------------------------------------------------------|
   |  SFK E-Book : A PDF optimized for your smart phone.      |
   |  SFK Plus   : Fast (x)replace, HTTPS web access and      |
   |               27 status lights in the system tray.       |
   |  DView Pro  : Search 10,000 text files per second.       |
   |               Fly over 100,000 files in one window.      |
   |----------------------------------------------------------|
   |             Read more on www.stahlworks.com              |
   +----------------------------------------------------------+

C:\Users\Mane\Downloads\Backup-sfk-main>sfk198.exe zip
sfk zip out[.zip] [opt] mydir [file1 file2 ...]
sfk zip out[.zip] [opt] -dir mydir -file file1 file2

   add files and folders to a .zip file.

   About filename encoding

   if filenames contain special chars like umlauts
   or accents the following applies:

   - under windows, sfk zip stores filenames

     1. in OEM codepage 437 of your system,
        to support old extraction tools.

     2. and as UTF-8, in the zip format 0x7075 extension
        which will be used by up-to-date programs.

   - under linux, sfk stores only one name, which is
     marked as UTF-8, if such encoding is detected.
     on any other encoding, like accent chars on old file
     systems, sfk zip stores characters as is, and later
     extraction may produce wrong names.

   - UTF-8 name extensions are supported only by up-to-
     date zip extraction tools, like 7zip, Windows 10
     File Explorer, or sfk unzip.

   - names with accent chars exchanged between Mac and
     Non-Mac systems may look wrong due to Decomposed
     Unicode used in Mac OS/X.

   if you extract files at the receiver, then open
   windows explorer and see unexpected filename
   characters, this means the receiver's unzip tool
   is old and does not understand UTF-8 extensions.

   - if you just see wrong accent characters
     it means the receiver system uses a different
     OEM codepage then the sender (sfk sysinfo).

   - if you see #Uxxxx it means filenames contain
     complex unicode chars, like asian or cyrillic.
     you can google for U+xxxx to see what character
     is actually meant.

   No update of existing content
     if the output zip file already exists
     then only new files which are not already
     contained can be added. sfk cannot update
     contents and times within existing zip files.

     sfk zip may fail to compare added filenames
     to existing names in a zip if name encodings
     are mixed or unclear, esp. on linux/mac.

   64 bit zip file support
     if contents are larger then 2 gb, sfk zip
     will create a 64 bit zip file automatically.
     not every unzip tool may be able to read this.
     SFK XE cannot read zip file contents over 2 gb.

   options
     -nosub    do not include sub folders.
     -force    overwrite existing zip file.
     -zipext   add .zip to output filename even
               if it already has an extension.
     -asdir x  create a new folder x within the zip
               and add all files into that folder.
               cannot add to an existing folder.
     -rel[names]  strip top level folder from
               filenames within the zip.
     -big      show a summary of largest files.
     -big=n    show a summary of n largest files.
     -old=n    show a summary of n oldest  files.
     -nosum    show no summary.
     -text     include only ascii text files
               but no binary files.
     -nometa   do not add the os/code comment,
               or set SFK_CONFIG=nozipmeta
     -setexec  mask1 mask2 !mask3 ...
               mark files as executable with
               linux/mac operating systems.
               must be followed by -dir ...
     -offtime  store file times which are
               one hour off, depending on DST.
               for details see: sfk help offtime

   output filename rendering
     if output filename does not contain '.'
     then '.zip' is added. use -zipext to add
     whenever if it does not contain .zip

   output chaining
     sfk zip supports text output chaining,
     to pass filenames for filtered display.

   see also
     sfk zipuni  use just UTF-8 filenames,
                 to support old linux tools.
     sfk unzip   extract a zip file.
     sfk zipto   zip files selected by a
                 previous command.

   sfk zip is very flexible and easy to use,
   but if you need special features like
   direct zip file updating you may consider
   further zipping tools. find an overview on:
   stahlworks.com/zip

   examples
     sfk zip out mydir !.bak
       add all contents of mydir into out.zip,
       except for .bak files, using the short
       file selection syntax.

     sfk zip out -dir foo bar -file !.bak
       add all contents of folder foo and folder
       bar into out.zip, except for .bak files,
       using the long file selection syntax.

     sfk zip out -dir mydir -subdir !save !\tmp
      -file !.bak !old
       add all of mydir into out.zip, except for
       sub folders having 'save' in their name or
       starting with 'tmp', and except for files
       with .bak extension or 'old' in their name.

     sfk select mydir .png +zipto out
       add all .png images of mydir to out.zip.

     sfk zip out mydir .png
       same as above, in one step.

     sfk zip out -since 3d mydir
       add files changed in the last three days.

     sfk zip out.zip -flist mylist.txt
       read a list of filenames from mylist.txt
       and add these files to out.zip

     sfk list -late=5 mydir +zipto out -force
       write the 5 newest files to out.zip,
       overwriting an existing out.zip

     sfk zip out -setexec /conf/ .sh -dir mydir
       zip mydir, mark files named exactly conf,
       or being in a folder conf, or having .sh
       in their name as executable on linux.

     sfk unzip -todir tmpdoc in.odt
     sfk zip -rel out.odt tmpdoc
       extract an openoffice writer document
       into a folder tmpdoc, then repack it to
       out.odt, without the tmpdoc folder name.

     sfk sel -sincedir proj1 proj2 +zipto out
       if proj2 is a newer copy of proj1,
       collect all files added or changed
       since proj1 into out.zip

     sfk zip out mydir +filter -!test
       pack mydir to out.zip, but do not print
       any names with "test" to terminal.
```