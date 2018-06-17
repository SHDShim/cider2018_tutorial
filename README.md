## Purpose of the tutorial

In the mineral physics tutorial at CIDER 2018, we will demonstrate typical data analysis for equation of state (EOS).  We then discuss reasonable ways to estimate uncertainties and propagate them for better use of EOS data.

Here I explain the necessary computer setups for the tutorial.

## Where to install

The CIDER 2018 tutorial will be given in a VirtualMachine file.  The installation instruction here is given for installing the tutorial materials in the VirtualMachine file.  Therefore, you do not need to install the materials separately following this instruction, if you obtain the VirtualMachine file.

However, if you want to have the tutorial materials in your local machine, you may follow this instruction.  In fact, in this way code will be executed much faster and you can continue enjoying python + jupyter setup for your data analysis in the future.

Note that the instruction here is NOT tested for Windows OS.  There should be some slight but important differences.  Please contact [Dan Shim](shdshim@gmail.com) for questions.

## Pre-requisite 

[Anaconda 3.6](https://www.anaconda.com/download/)

You need to have Anaconda distribution of python installed in your virtualmachine or your local hard drive.  If not, please download the version above and install.  

Note that `Graphical installer` is easier if you have Mac OSX (also windows I believe).  For Linux, I found that the `command line` option works better.

## Update anaconda

Once you finish installation, you may update the anaconda package.

1. Run `terminal.app` or `console`.

2. Run anaconda `base` or `root` environment (Note that you do not need to type the commands below.  You may just copy and paste in the terminal.  This applies to all other commands below).
   ```bash
   source activate base
   ```
   
3. Run the following for updating anaconda.
   ```bash
   conda update --all
   ```

## Pytheos

The tutorial materials require the `pytheos` module.  You can install it simply by executing the following command in the terminal.

```bash
pip install pytheos
```

## Pytheos Jupyter Notebook examples

Tutorial materials are in `jupyter notebook``.  

1. Under your home folder, make a new directory and move to the directory
   ```bash
   mkdir EOS_tutorial1
   cd EOS_tutorial1
   ```
   
2. Install pytheos tutorial (don't forget the period at the end of the command below).
   ```bash
   git clone https://github.com/SHDShim/pytheos.git .
   ```
   
## Data analysis examples

We also use the data analysis we presented in Ye et al. (2017) JGR in Jupyter notebook in the tutorial.

1. Go back to your home folder, make a separate folder, and move to the folder.
   ```bash
   cd ~
   mkdir EOS_tutorial2
   cd EOS_tutorial2
   ```
   
2. Install the jupyter notebook files.
   ```bash
   git clone https://github.com/SHDShim/cider2018_tutorial.git .
   ```
   
Now you are all set!

## Reference

[Pytheos Github](https://github.com/SHDShim/pytheos) 

[Pytheos documentation](https://shdshim.github.io/pytheos-docs/) 

