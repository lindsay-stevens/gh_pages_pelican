Title: Projects
Date: 2024-07-29


The following are examples projects where I've applied my skills to deliver solutions.


## PyODK Library

Working with GetODK, I implemented a new Python library for interacting with the ODK Central data management platform. This new standardised method of interacting with project data has been widely adopted by the ODK community, being built upon in numerous other libraries and project-specific solutions.


## XLSForm/pyxform Maintenance

Working with GetODK, I implemented features, bug fixes, and other improvements to the XLSForm/pyxform project. Pyxform is a Python app / library which is used to convert data collection designs from a spreadsheet format into a machine-readable XML (XForm) format. XForms may then be used with compatible software to collect data, as an alternative to the time and expense of developing custom data management software. XForm-compatible products include the Nafundi / ODK platform, OpenClinica, among others.

The Pyxform code base is over 10 years old and has been maintained or contributed to by many different developers. It was previously compatible with Python 2 and 3 (now only 3), and has undergone numerous refactorings. These factors presented challenges in understanding the code history, both in terms of navigating version control history and in terms of requirements (intended, conflicting, or reverted designs), to avoid regressions and improve code quality and test coverage.


## OpenClinica Insight Product

I designed and implemented an ETL and reporting system that streamlines reporting and analysis workflows for dozens of OpenClinica customers and their numerous research projects. The system is primarily implemented in Python, with PostgreSQL using SQL and PL/PGSQL; some components include Clojure and bash scripts.

The OpenClinica system is underpinned by a form data collection and management operational database. Among many other features, forms are designed by users, can be version controlled, can be organised into visits, and each form element can be annotated or queried.

The Insight system transforms common data models for ease of reporting, and uses the metadata to dynamically generate data tables corresponding to user-specified form element groups. The transformation process incorporates strict data consistency and validations, and applies data refreshes in a performant way that minimises interruption to end users.


## Obstetrics Medical Records Analysis

As part of my Masters of Biostatistics, for a non-coursework project unit I analysed Obstetrics medical records data from the Sydney NSW Local Health District Obstetrics department database and medical record. The project was supervised by a Professor and a post-doc researcher from an epidemilogy unit at the University of Sydney, as well as a statistics Senior Lecturer from Macquarie University. The analysis was conducted with SAS and LaTeX, involved writing custom macros, and produced a detailed report document with data tables, charts, and interpretation.

The analysis described the characteristics of women who had consecutive singleton pregnancies with a term over 20 weeks, comparing those with and without gestational diabetes mellitus (GDM) in the second observed pregnancy. The main exposures of interest were the duration of the inter-pregnancy interval (IPI), and the change in BMI. The main techniques used was logistic regression.

The analysis found that high initial BMI, weight gain, and longer than recommended IPI were associated with increased odds ratios for GDM in the second pregnancy. There was interaction between initial BMI and the BMI change, and initial BMI and IPI, suggesting that the effect of the exposures on GDM is amplified for overweight women. The findings were consistent with GDM diagnosis criteria, and previous research that investigated alternative combinations of these factors.


## Breast Cancer Registry Analysis

As part of my Masters of Biostatistics, for a non-coursework project unit I analysed Breast Cancer data from the Auckland Breast Cancer Register. The project was supervised by a statistics Lecturer at Macquarie University, and a breast cancer surgeon at Bankstown-Lidcombe Hospital who had proposed the project. The analysis was conducted with Stata and LaTex, involved writing custom Stata modules, and produced a detailed report document with data tables, charts, and interpretation.

The analysis described differences in characteristics of women with breast cancer detected by screening (comparing by age at initial diagnosis, 45-69 years vs. 70+), and assessed whether baseline variables affected the association between age group and 5-year breast cancer mortality. The main techniques were Pearson Chi-squared and Cox Proportional Hazards models.

The analysis found that in general screening continued to detect similar disease profiles after 70, similar treatment combinations were used, and the strongest associations for 5-year survival were with age and disease grade. In the context of NZ breast cancer screening programs that end at age 70, these findings suggested that there may be some merit to extending these programs.


## Mobile Data Collection

I designed and implemented a mobile data collection framework that improved quality and completeness of participant questionnaire data for 5 projects conducted by the VHCRP team at the Kirby Institute.

The framework covered all aspects - policies for device procurement, configuration, management, account management and security; tools for form design, validation, multi-language capable presentation customisation; procedures for data collection, submission, and storage; tools for ETL of collected data for analysis in Stata.

The deployment included over 80 Android tablets for offline data collection at study sites, including hospitals, clinics and prisons in Australia and internationally, with thousands of responses from hundreds of participants had been collected and processed. At the centre of the framework was ODK Collect, an Android app for processing XML-based form definitions. Design and data processing tools included custom distributable desktop apps written in Python.


## OpenClinica Community DataMart

I designed and implemented an ETL and reporting system that streamlined reporting and analysis workflows for 13 projects conducted by the VHCRP team at the Kirby Institute. This system was implemented with PostgreSQL using SQL and PL/PGSQL.

This system replaced a time-intensive process involving numerous manual steps, with a robust, automated process. The ETL system involved transforming a column-based data storage format into user-friendly tables corresponding to the original form design templates uploaded to OpenClinica.

The deployment included encrypted connections between database servers and with client machines, data access controls mirroring those in OpenClinica, and integrated Windows domain authentication. Client tools were also developed to integrate via ODBC with Stata, SAS and Microsoft Access; as well as automated VBScript tools to simplify setup for new users. The preparation of detailed documentation and delivery of targeted training encouraged adoption of the system across the team.


## System Integrations

I designed and implemented the following system integrations for the VHCRP team at the Kirby Institute:

- An automated daily transfer of hepatitis C test results from a LabKey sample management database to the clinical database in OpenClinica. Written in Python, and included development of a re-usable library for interacting with OpenClinica's SOAP XML webservices.
- A promotional website for a study with a custom styled LimeSurvey instance for web-based data collection from study participants. Written in Python and JavaScript and included development of a re-usable library for interacting with LimeSurvey's REST JSON webservices.
- An automated integration test suite for the above custom LimeSurvey template to ensure that these elements worked as expected across common browsers. Written in Python using Selenium WebDrivers for Firefox, Chrome and Internet Explorer.
