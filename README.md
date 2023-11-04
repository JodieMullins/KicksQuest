# Kicks Quest - A Capstone Project

This repository holds an examination of a small business over the course of approximately three years. All data has been created using Mockaroo.com and Google Sheets, as well as some csv-json conversion websites. The data does not reflect real people or events and is curated for the use of this particular project and specific operations performed therein to complete the requirements of Code:You's Module 4 Capstone for the May 2023 Data Analysis cohort.  

The idea is based upon a custom shoe design company that profits from hand-designing originally plain pairs of high-quality shoes. Sometimes this company also sells handmade adornment pieces to display upon a pair of shoes rather than a whole new pair. 

--------------------------------------------------------------------------------------------------------------

### Features Included

1. Examine 3+ data files and file formats (easy);  establish local database and read data in with SQLite (hard)
2. Clean data / perform pandas merge with 2+ datasets, calculate new values (intermediate)
3. Make 3+ matplotlib visualizations (easy); Tableau dashboard (intermediate)
4. Virtual Environment & Instructions included in README below (intermediate); .gitignore file included; 5+ distinct commits
5. Annotation with markdown in Jupyter Notebook & well-documented code (intermediate)

--------------------------------------------------------------------------------------------------------------

## Virtual Environment

This project was written in Python Version 3.10 with an update to 3.12; on the same system exists Anaconda Version 3.11. You may open a conda environment, but these instructions assume the user only has Python 3.10+ installed and will be using the VS Code Python Extension.

When one opens the primary file that is the Jupyter Notebook (*KicksQuest_Notebook*.ipynb), the first block includes all libraries necessary to run my project. If your computer system contains similiarly updated libraries, you may possibly run the files here without a virtual environment successfully. 

However, in any case, the necessary libraries have been documented in the requirements.txt. Given that the versions of the libraries I used to create my project on my system may not exactly be the same as the libraries installed on someone else's computer system, I have opted to include Virtual Environment instructions as follows: 

If you choose the method of opening in **VS Code**:

1. First, open a clean, new file in VS Code.
2. Open the terminal window
    * Look for the square containing ***>_*** on the left-hand panel.
    * Half-way down / towards the bottom of the input area to find the Terminal Window

3. Type >`cd 'C:file\path\to find\project\folder'`
      * Note: instead of typing out the whole line, you may copy and paste the file path from the address bar inside the opened project folder

4. To establish a virtual environment folder, type >`python -m venv venv`
    * (where the second venv is the name of the folder for the environment)
5. Activate the environment by typing:
    * **WINDOWS** *PowerShell* >`<venv>\scripts\activate`
    * **WINDOWS** *cmd* >`<venv>\Scripts\activate.bat`
    *  **LINUX** *bash/zsh* $`source <venv>/bin/activate`
6. A new, colorful text will appear in front of the file path displaying that you've successfully activated the environment. 

7. Type >`pip install jupyter`
     * This will likely take a moment.
8. Type >`pip install -r requirements.txt`
9. Type >`jupyter notebook`
    * Eventually, a default browser window will open. From here, you may upload the project notebook from the project folder into the Jupyter instance established. 


***If you wish to proceed in VS Code***:
-------------------------------------------

1) Return to VS Code and press on the Keyboard `Ctrl+Shift+P`

    * `Cmd+Shift+P` on Mac 

2) In the very top bar of VS Code, type `Python: Select Interpreter` and press enter

3) Here, you will be given a range of environments to choose from. Choose 'venv' from this drop-down menu to operate within the virtual environment established.

4) You may 'Run' all cells of the notebook and exit when ready.


***If you want to proceed in the browser***: 
---------------------------------------------

1) Click the box next to the notebook's name for a checkmark and locate the 'Open' option under the 'Files' tab.
    
    * Note: it may work best to keep the 'Home' tab open for now.

2) When the new tab for the notebook opens, select the most appropriate kernel / no kernel 
    
    * Typical selection may be "Python 3 ipykernel" if user has Anaconda installed

3) Find the 'Run' drop-down menu to select 'Restart Kernel and Run All Cells...'

4) Once done with the Jupyter notebook, remember to select the 'Home' tab, then 'Running' to click 'Shut Down All' and 'X' out of all tabs.

--------------------------------------------