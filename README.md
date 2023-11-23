# Kicks Quest - A Keystone Project

This repository holds an examination of a small business over the course of approximately three years. All data has been created using Mockaroo.com and Google Sheets, as well as some csv-json conversion websites. The data does not reflect real people or events and is curated for the use of this particular project and specific operations performed therein to complete the requirements of Code:You's Module 4 Capstone for the May 2023 Data Analysis cohort.  

The idea is based upon a custom shoe design company that profits from hand-designing originally plain pairs of high-quality shoes. Sometimes this company also sells handmade adornment pieces to display upon a pair of shoes rather than a whole new pair. 

The data specifically examines profitability of all years in business with a special interest in determining a general yet logical storefront location. Results of the data include items such as an email list, a profit statement by state, a folder of graphs/charts, and a logical implication for a general location of a future storefront.

--------------------------------------------------------------------------------------------------------------

### Features Included

1. Examine 3+ data files and file formats (easy);  establish local database and read data in with SQLite (hard)
2. Clean data / perform pandas merge with 2+ datasets, calculate new values (intermediate)
3. Make 3+ matplotlib visualizations (easy); Tableau dashboard (intermediate)
4. Virtual Environment & Instructions included in README below (intermediate); .gitignore file included; 5+ distinct commits
5. Annotation with markdown in Jupyter Notebook & well-documented code (intermediate)

--------------------------------------------------------------------------------------------------------------

### To Run Project:

1. Clone KicksQuest repository to local machine (manually or via  **VS Code**)
2. If not using a virtual environment:
    * Open Folder using **VS Code**.
    * Select the *KicksQuest_Notebook*.ipynb document from the Explorer side panel.
    * To automatically execute all the cells in the Jupyter Notebook, click "Run All" when viewing the notebook in the editing window **OR** 'Run and Debug' (the bug on an assumed triangle) option from the left-hand Explorer panel.
    * Alternatively to running all of the cells at once, the user may run each cell individually by selecting the sideways triangle icon beside each input square.

Note: I also have a [Demo repo](https://github.com/JodieMullins/CY-Demo) available for a general idea of the output this Capstone project will produce for those that would like to see what this project does without cloning it or running any code at all.


--------------------------------------------------------------------------------------------------------------

## Virtual Environment

This project was written in Python Version 3.10 with an update to 3.12; on the same system exists Anaconda Version 3.11. User may open a conda environment, but these instructions assume the user only has Python 3.10+ installed and will be using the VS Code Python Extension.

When one opens the primary file that is the Jupyter Notebook (*KicksQuest_Notebook*.ipynb), the first block includes all libraries necessary to run my project. If the user's computer system contains similiarly updated libraries, one may possibly run the files here without a virtual environment successfully. 

However, in any case, the necessary libraries have been documented in the requirements.txt. Given that the versions of the libraries I used to create my project on my system may not exactly be the same as the libraries installed on someone else's computer, I have opted to include Virtual Environment instructions as follows: 

Ensure the repository has been cloned from GitHub to the local machine / AKA download a local copy of the files from online to user's computer. This is because the user will need to locally establish and activate one's own virtual environment within the project folder.


If choosing the method of opening in **VS Code**:

1. First, open a clean, new file in VS Code.
2. Open the terminal window
    * Look for the square containing **>_** on the left-hand panel.
    * Half-way down / towards the bottom of the input area to find the Terminal Window

3. Type (on Windows) >`cd 'C:file\path\to find\project\folder'`
      * Mac: >`cd /path/to/project/folder/from/root`
      * Note: On Windows, instead of typing out the whole line, user may copy and paste the file path from the address bar inside the opened project folder

4. To establish a virtual environment folder, type >`python -m venv venv`
    * (where the second venv is the name of the folder for the environment)
5. Activate the environment by typing:
    * **WINDOWS** *PowerShell* >`<venv>\scripts\activate`
    * **WINDOWS** *cmd* >`<venv>\Scripts\activate.bat`
    * **LINUX/Mac** *bash/zsh* $`source <venv>/bin/activate`
6. A new, colorful text will appear in front of the file path meaning the user has successfully activated the environment. 

7. Type >`pip install jupyter`
     * This will likely take a moment.
8. Type >`pip install -r requirements.txt`
9. Type >`jupyter notebook`
    * Eventually, a default browser window will open. From here, the user may upload the project notebook from the project folder into the preferred Jupyter instance. 


***To proceed in VS Code***:
-------------------------------------------

1) Return to VS Code and press on the Keyboard `Ctrl+Shift+P`

    * `Cmd+Shift+P` on Mac 

2) In the very top bar of VS Code, type `Python: Select Interpreter` and press enter

3) Here, the user will be given a range of environments to choose from. Choose 'venv' from this drop-down menu to operate within the virtual environment established.

4) The user may 'Run' all cells of the notebook and exit when ready.


***To proceed in the browser ***: 
---------------------------------------------

1) Click the box next to the notebook's name for a checkmark and locate the 'Open' option under the 'Files' tab.
    
    * Note: it may work best to keep the 'Home' tab open for now.

2) When the new tab for the notebook opens, select the most appropriate kernel / no kernel 
    
    * Typical selection may be "Python 3 ipykernel" if user has Anaconda installed

3) Find the 'Run' drop-down menu to select 'Restart Kernel and Run All Cells...'

4) Once done with the Jupyter notebook, remember to select the 'Home' tab, then 'Running' to click 'Shut Down All' and 'X' out of all tabs.

--------------------------------------------
