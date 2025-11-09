---
hide:
  - footer
title: Deploying Django
---

# Deploying Django

Building a Django project that works on your system is satisfying, but it gets even more satisfying when you see your site deployed where anyone can access it.

In the second half of Chapter 20, the book walks you through the process of deploying to the hosting company Platform.sh. That company has rebranded as [Upsun](https://upsun.com), and they've changed their approach to deployment somewhat. The printed instructions no longer work for deployment, but the instructions here are fully up to date. If you run into any steps that don't seem to work, please [reach out](../contact.md) and I will update these instructions. Thank you!

## Making an Upsun Account

To make an account, go to [https://upsun.com](https://upsun.com) and click the Free Trial button. Currently, Upsun offers a 15-day free trial.

## Flex and Fixed plans

Upsun offers two types of deployment plans, *Flex* and *Fixed*. With a Flex plan, you can adjust the size of individual resources as your project grows. With Fixed plans, you choose an overall set of resources, and then you can upgrade those resources as a group when your project grows.

Upsun steers people towards Flex plans, but it's more expensive and not needed when you're first learning to deploy a small project.

### Adding a Fixed Organization

When you create an account on Upsun, you also create an *Organization* on their Flex plan. Make a new Organization on the Fixed plan by clicking the drop down arrow next to My Projects on the dashboard, and then clicking **New organization**:

![The dialog for adding a new organization on Upsun](../images/upsun_new_org_dialog.png)

In the **Create organization** dialog that appears, make a name for your new organization. I used the form `<first_name>_fixed`. Make sure to change the **Organization type** to "Fixed".

![The create organization form on Upsun](../images/upsun_create_org_form_bordered.png)

Click the **Create organization** button, and you should see a clear indication that your organization is set up use Upsun's Fixed resources:

![Organization page showing "Fixed"](../images/upsun_fixed_org_bordered.png)

The Upsun CLI
---

To deploy and manage a project on Platform.sh, you’ll need the tools available in the Command Line Interface (CLI). To install the latest version of the CLI, visit [https://docs.upsun.com/administration/cli.html](https://docs.upsun.com/administration/cli.html) and follow the instructions for your operating system. If you're on Windows and haven't installed something like this in a terminal before, I recommend using [Scoop](https://scoop.sh). Scoop makes it easy to install the Upsun CLI, and many other tools you might find helpful as you continue working on more complex programming projects.

Creating a *requirements.txt* file
---

The remote server needs to know which packages Learning Log depends on, so we’ll use pip to generate a file listing them. Again, from an active virtual environment, issue the following command:

```sh
(ll_env)learning_log$ pip freeze > requirements.txt
```

The freeze command tells pip to write the names of all the packages currently installed in the project into the file *requirements.txt*. Open this file to see the packages and version numbers installed in your project:

```txt
asgiref==3.10.0
django==5.2.8
django-bootstrap5==25.2
sqlparse==0.5.3
```

Learning Log already depends on specific versions of four different packages, so it requires a matching environment to run properly on a remote server. (We installed two of these packages manually, and two others were installed automatically as dependencies of these packages.)

When we deploy Learning Log, Upsun will install all the packages listed in *requirements.txt*, creating an environment with the same packages we’re using locally. Because of this, we can be confident the deployed project will function just like it has on our local system. This approach to managing a project is critical as you start to build and maintain multiple projects on your system.

Using Git to Track the Project's Files
---

As discussed in Chapter 17, Git is a version control program that allows you to take a snapshot of the code in your project each time you implement a new feature successfully. If anything goes wrong, you can easily return to the last working snapshot of your project; for example, if you accidentally
introduce a bug while working on a new feature. Each snapshot is called a *commit*.

Using Git, you can try implementing new features without worrying about breaking your project. When you’re deploying to a live server, you need to make sure you’re deploying a working version of your project. To read more about Git and version control, see Appendix D.

### Installing Git

Git may already be installed on your system. To find out, open a new terminal window and issue the command `git --version`:

```sh
(ll_env)learning_log$ git --version
git version 2.51.0
```

If you get a message indicating that Git is not installed, see the installation instructions in Appendix D.

### Configuring Git

Git keeps track of who makes changes to a project, even when only one person is working on the project. To do this, Git needs to know your username and email. You must provide a username, but you can make up an email for your practice projects:

```sh
(ll_env)learning_log$ git config --global user.name "eric"
(ll_env)learning_log$ git config --global user.email "eric@example.com"
```

If you forget this step, Git will prompt you for this information when you make your first commit.

### Ignoring Files

We don’t need Git to track every file in the project, so we’ll tell it to ignore some files. Create a file called *.gitignore* in the folder that contains *manage.py*. Notice that this filename begins with a dot and has no file extension. Here’s the code that goes in *.gitignore*:

```txt
.gitignore ll_env/
__pycache__/
*.sqlite3
```

We tell Git to ignore the entire *ll_env* directory, because we can re-create it automatically at any time. We also don’t track the *\__pycache__* directory, which contains the *.pyc* files that are created automatically when the *.py* files are executed. We don’t track changes to the local database, because it’s a bad habit: if you’re ever using SQLite on a server, you might accidentally overwrite the live database with your local test database when you push the project to the server. The asterisk in `*.sqlite3` tells Git to ignore any file that ends with the extension *.sqlite3*.

!!! note
    If you’re using macOS, add *.DS_Store* to your *.gitignore* file. This is a file that stores information about folder settings on macOS, and it has nothing to do with this project.

### Committing the Project



old
---

 Platform.sh has a free tier that, as of this writing, does not require a credit card. The trial period allows you to deploy an app with minimal resources, which lets you test your project in a live deployment before committing to a paid hosting plan.