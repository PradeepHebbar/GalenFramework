package com.brillio.utility;

import java.awt.AWTException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import net.mindengine.galen.api.Galen;

public class prepareSpecs extends galenTestBase {
	static StringTokenizer st1;
	static String msg;
	public static String inp = "";

	/**
	 * @param driver
	 * @param URL
	 * @param ipSpec
	 * @throws IOException
	 * @throws AWTException
	 * @throws InterruptedException
	 */
	public void generateSpecs(WebDriver driver, String URL, String ipSpec)
			throws IOException, AWTException, InterruptedException {
		prepareSpecs.generateInputSpecs(driver, URL, ipSpec);
		prepareSpecs.generateDumpFile(driver, URL, ipSpec);
	}

	/**
	 * @param driver
	 * @param URL
	 * @param ipSpec
	 * @throws IOException
	 */
	public static void generateInputSpecs(WebDriver driver, String URL, String ipSpec) throws IOException {
		List<WebElement> allLocators = driver.findElements(By.xpath(".//*"));
		File file1 = new File("specs/inputSpecs/" + ipSpec + ".spec");
		if (!file1.exists()) {
			file1.createNewFile();
		}
		FileWriter fw = new FileWriter(file1.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);
		String chtxt1 = null;
		bw.write("====================================================================");
		bw.newLine();
		String delims1 = "\n";
		int count = 0;
		for (WebElement locator : allLocators) {
			chtxt1 = locator.getAttribute("id").toString();
			st1 = new StringTokenizer(chtxt1, delims1);
			while (st1.hasMoreElements()) {
				count++;
				msg = (String) st1.nextElement();
				bw.newLine();
				inp += "    " + msg + "   id   " + msg + "\n";
				bw.write("    " + msg + "   id   " + msg);
			}
			if (count > 80) {
				System.out.println("Input spec with maximum 80id's are created");
				break;
			}

		}
		bw.newLine();
		bw.close();
		System.out.println("Input spec created sucessfull");
		System.out.println("Input spec created at: " + "specs/inputSpecs/" + ipSpec + ".spec");

	}

	/**
	 * @param driver
	 * @param URL
	 * @param ipSpec
	 * @throws IOException
	 * @throws AWTException
	 * @throws InterruptedException
	 */
	public static void generateDumpFile(WebDriver driver, String URL, String ipSpec)
			throws IOException, AWTException, InterruptedException {
		WebDriver dumpDriver;
		System.setProperty("webdriver.chrome.driver", "drivers/chromedriver.exe");
		Galen.dumpPage(driver, URL, "specs/inputSpecs/" + ipSpec + ".spec", "dumps/" + ipSpec);
		dumpDriver = new ChromeDriver();
		dumpDriver.manage().window().maximize();
		dumpDriver.get("E:\\EclipseMars\\EclipseWorkspace\\galenNew\\dumps\\" + ipSpec + "\\page.html");
		prepareSpecs.generateoutPutSpec(dumpDriver, URL, ipSpec);
		dumpDriver.close();
	}

	/**
	 * @param driver
	 * @param URL
	 * @param ipSpec
	 * @throws IOException
	 * @throws InterruptedException
	 */
	private static void generateoutPutSpec(WebDriver driver, String URL, String ipSpec)
			throws IOException, InterruptedException {
		List<WebElement> allitems = driver.findElements(By.xpath(".//*[@id='object-list']/ul/li"));
		for (WebElement element : allitems) {
			element.click();
		}

		WebElement specs = driver.findElement(By.xpath(".//*[@id='object-suggestions']/div"));
		WebElement childs = specs.findElement(By.xpath(".//*"));
		File file = new File("specs/outputSpecs/" + ipSpec + ".spec");
		if (!file.exists()) {
			file.createNewFile();
		}

		List<String> startContent = readLines("specs/inputSpecs/" + ipSpec + ".spec");
		String content = childs.getText();
		String contentArray[] = content.split("\n\n");
		for (String arrayElements : contentArray) {
			boolean header = true;
			String delims = "\n";
			StringTokenizer st = new StringTokenizer(arrayElements, delims);
			while (st.hasMoreElements()) {
				String msg = (String) st.nextElement();

				if (header) {
					String abc = "=" + msg + "=" + "\n";
					abc=abc.replace(":", "");
					msg = abc + "\t" + msg;
					header = false;
				} else {
					msg = "\t" + msg;
				}
				if (msg.contains("e+3%")) {
					String msg1 = msg.replace("e+3%", "%");
					startContent.add(msg1);
				} else if (msg.contains("Infinity%")) {
					String msg2 = msg.replace("Infinity%", "~10%");
					startContent.add(msg2);
				} else if (msg.contains("NaN%")) {
					String msg3 = msg.replace("NaN%", "~0%");
					startContent.add(msg3);
				}

				else {
					startContent.add(msg);
				}

			}
		}

		FileUtils.writeLines(file, startContent);
		System.out.println("OutPut spec created sucessfull");
		System.out.println("OutPut spec created at: " + "specs/OutputSpecs/" + ipSpec + ".spec");

	}

	/**
	 * @param filename
	 * @return
	 * @throws IOException
	 */
	private static List<String> readLines(String filename) throws IOException {
		FileReader fileReader = new FileReader(filename);
		BufferedReader bufferedReader = new BufferedReader(fileReader);
		List<String> lines = new ArrayList<String>();
		String line = null;
		lines.add("@objects");
		boolean isstartindexfound = false;
		while ((line = bufferedReader.readLine()) != null) {
			if (line.equalsIgnoreCase("")) {
				isstartindexfound = !isstartindexfound;
			}
			if (isstartindexfound) {
				lines.add("\t" + line);

			}
		}
		lines.add("@on [desktop]");
		lines.add("\n");
		bufferedReader.close();

		return lines;

	}

}
