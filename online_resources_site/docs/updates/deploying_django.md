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







old
---

 Platform.sh has a free tier that, as of this writing, does not require a credit card. The trial period allows you to deploy an app with minimal resources, which lets you test your project in a live deployment before committing to a paid hosting plan.