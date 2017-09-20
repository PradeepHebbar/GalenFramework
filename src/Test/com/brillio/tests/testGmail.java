package com.brillio.tests;

import java.awt.AWTException;
import java.io.IOException;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;
import com.brillio.utility.galenTestBase;
import com.brillio.utility.prepareSpecs;

public class testGmail extends galenTestBase {
	static WebDriver driver;
	
	@Test(dataProvider = "devices")
	public void checkLayoutGmail(TestDevice device) throws InterruptedException, IOException, AWTException {
		prepareSpecs obj = new prepareSpecs();
		driver = galenTestBase.driver;
		obj.generateSpecs(driver, driver.getCurrentUrl(), "gmailLogin" + device.uniqueID());
		try {
			checkLayout("specs/outputSpecs/gmailLogin" + device.uniqueID() + ".spec", device.getTags());
		} catch (Exception e) {

		}
		driver.findElement(By.xpath("//input[@id='Email']")).sendKeys("pradeephebbar93");
		driver.findElement(By.xpath("//input[@id='next']")).click();
		Thread.sleep(3000);
		obj.generateSpecs(driver, driver.getCurrentUrl(), "gmailPassword" + device.uniqueID());
		try {
			checkLayout("specs/outputSpecs/gmailPassword" + device.uniqueID() + ".spec", device.getTags());
		} catch (Exception e) {

		}

	}
}
