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

To deploy and manage a project on Platform.sh, you’ll need the tools available in the Command Line Interface (CLI). To install the latest version of the CLI, visit https://docs.platform.sh/development/cli.html and follow the instructions for your operating system.

On most systems, you can install the CLI by running the following command in a terminal:

```sh
$ curl -fsS https://platform.sh/cli/installer | php
```

N O T E After this command has finished running, you will need to open a new
terminal window before you can use the CLI.





old
---

 Platform.sh has a free tier that, as of this writing, does not require a credit card. The trial period allows you to deploy an app with minimal resources, which lets you test your project in a live deployment before committing to a paid hosting plan.