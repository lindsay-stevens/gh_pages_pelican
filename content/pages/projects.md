Title: Projects
Date: 2018-07-15


The following are examples projects where I've applied my skills to deliver solutions.


## Mobile Data Collection

I designed and implemented a mobile data collection framework that improved quality and completeness of participant questionnaire data for 5 projects conducted by the VHCRP team at the Kirby Institute.

The framework covered all aspects - policies for device procurement, configuration, management, account management and security; tools for form design, validation, multi-language capable presentation customisation; procedures for data collection, submission, and storage; tools for ETL of collected data for analysis in Stata.

The deployment included 83 Android tablets for offline data collection at study sites, including hospitals, clinics and prisons in Australia and internationally, with thousands of responses from hundreds of participants had been collected and processed. At the centre of the framework was ODK Collect, an Android app for processing XML-based form definitions. Design and data processing tools included custom distributable desktop apps written in Python.


## OpenClinica Community DataMart

I designed and implemented an ETL and reporting system that streamlined reporting and analysis workflows for 13 projects conducted by the VHCRP team at the Kirby Institute.

This system replaced a time-intensive process with numerous manual steps, with a robust, automated process that integrated with existing reporting and analysis tools while maintaining a high level of security and ease of use.

This system was implemented with PostgreSQL using SQL, PL/PGSQL, and Python. The ETL system involved transforming a column-based data storage format into user-friendly tables corresponding to the original form design templates uploaded to OpenClinica.

The deployment included encrypted connections between database servers and with client machines, data access controls mirroring those in OpenClinica, and integrated Windows domain authentication. Client tools were also developed to integrate via ODBC with Stata, SAS and Microsoft Access; as well as automated VBScript tools to simplify setup for new users. The preparation of detailed documentation and delivery of targeted training encouraged adoption of the system across the team.


## System Integrations

I designed and implemented the following system integrations for the VHCRP team at the Kirby Institute:

- An automated daily transfer of hepatitis C test results from a LabKey sample management database to the clinical database in OpenClinica. Written in Python, and included development of a re-usable library for interacting with OpenClinica's SOAP XML webservices.
- A promotional website for a study with a custom styled LimeSurvey instance for web-based data collection from study participants. Written in Python and JavaScript and included development of a re-usable library for interacting with LimeSurvey's REST JSON webservices.
- An automated integration test suite for the above custom LimeSurvey template to ensure that these elements worked as expected across common browsers. Written in Python using Selenium WebDrivers for Firefox, Chrome and Internet Explorer.
