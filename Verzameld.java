import java.io.*;
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

import java.util.Date;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Verzameld {
	
	private static final Logger log = Logger.getLogger( Verzameld.class.getName() );
	private static FileHandler fh = null;

	public static void main( String[] args) {
		try {
			initLog();
			log.log( Level.FINER, "Start logging to file.");
			System.out.println("Verzameld werk start");
			// FileWriter writes characters to file
			System.out.println("Type timestamp UNIX Epoch" );
			String s = new BufferedReader(new InputStreamReader (System.in)).readLine();
			long time = Long.parseLong(s);
			String date = convertUnixTimeToDate(time);
			System.out.println("Time was: " + date);
		}
		catch (Exception e) {
			System.out.println("Verzameld werk exception: " + e);
		}
	}

    public static void initLog(){
		try {
			fh=new FileHandler("C:\\tmp\\test.log", true);
		} catch (SecurityException | IOException e) {
			e.printStackTrace();
		}
    	fh.setFormatter(new SimpleFormatter());
    	log.addHandler(fh);
    	log.setLevel(Level.FINEST);
    }
    
	public void allFunctions() throws Exception {
		// Create and delete a file
		File xFile = new File("x.txt");
		xFile.createNewFile();
		if (xFile.exists()) {
			System.out.println("File exists");
			String type = xFile.isFile() ? "File " : "Directory ";
			String name = xFile.getCanonicalPath();
			long leng = xFile.length();
			System.out.println("File "+name+" has type "+type+" of size "+leng);
		} else {
			System.out.println("File notexists");
		}
		xFile.delete();
		
		// Display current dir
		String currydir = System.getProperty("user.dir");
		System.out.println("Current dir = "+currydir);
		File currentdir = new File(currydir);
		String [] fileList = currentdir.list();
		for (int i=1; i<fileList.length; i++)
			System.out.println(" "+fileList[i]);
		
		File tmpDir = new File("temp");
		tmpDir.mkdir();
		File newFile = new File(tmpDir+"/xxx.txt");
		if ( !newFile.exists() || !newFile.canRead()) {
			System.out.println("Can't read this file "+newFile );
			newFile.createNewFile();
		}

		// FileWriter writes characters to file
		System.out.println("Type something" );
		String s = new BufferedReader(new InputStreamReader (System.in)).readLine();
		File out = new File(tmpDir+"/output.txt");
		FileWriter fw = new FileWriter (out);
		PrintWriter pw = new PrintWriter(fw);
		pw.println(s);
		fw.close();
		
		// "wait a moment" stops the app and waits for a return on the command line
		while (true) {
			System.out.println("Please press enter to continue");
			char c = (char)System.in.read();
			if (c == '\n') {     
				break;
			}
		}

	    // run a command
	    String unixcommand = "ps -ef";
	    String outlist[] = runCommand(unixcommand);

	    // display its output
	    for (int i = 0; i < outlist.length; i++) {
	    	if (outlist[i].substring(0,8).equals(" etmrisc")) {
		    	if (outlist[i].substring(47,56).equals("/usr/java"))
		        System.out.println(outlist[i].substring(9,14));
		    }
		    if (outlist[i].substring(0,8).equals(" etmrisc")) System.out.println(outlist[i]);

		}

		// write the PID in the lockfile
		String lockFile = "lock.txt";
		int pid = 22;
		String spid = String.valueOf(pid);
		FileWriter myWriter;
		BufferedWriter dateFileStore;
		myWriter = new FileWriter(lockFile);
		dateFileStore = new BufferedWriter(myWriter);
		dateFileStore.write(spid,0,spid.length());
		dateFileStore.flush();
		dateFileStore.close();

//		// Touch the lock file to show that we are still active
//		File lf = new File(lockFile);
//		if (!ConcurrentCollector) {
//			try {
//				lf.setLastModified(System.currentTimeMillis());
//				log.debug("New timestamp set on lock file " + lf.lastModified());
//			} catch (Exception e) {
//				log.error("Cannot set new timestamp on lock file. Continuing.");
//			}
//		}
	}
	
	static public String convertUnixTimeToDate(long time){
	    java.util.Date date = new Date(time);
	    Format format = new SimpleDateFormat("yyyy MM dd HH:mm:ss");
	    return format.format(date);
	}
	

	static public String[] runCommand(String cmd)
		throws IOException {

		// set up list to capture command output lines

		ArrayList list = new ArrayList();

		// start command running

		Process proc = Runtime.getRuntime().exec(cmd);

		// get command's output stream and
		// put a buffered reader input stream on it

		InputStream istr = proc.getInputStream();
		BufferedReader br =
			new BufferedReader(new InputStreamReader(istr));

		// read output lines from command

		String str;
		while ((str = br.readLine()) != null)
			list.add(str);

		// wait for command to terminate

		try {
			proc.waitFor();
		}
		catch (InterruptedException e) {
			System.err.println("process was interrupted");
		}

		// check its exit value

		if (proc.exitValue() != 0)
			System.err.println("exit value was non-zero");

		// close stream

		br.close();

		// return list of strings to caller

		return (String[])list.toArray(new String[0]);
	}
}