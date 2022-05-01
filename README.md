# Esi_lecture with Odoo
Esi_lecture is a project using the odoo ERP. 
This project consists in having access to a multitude of books, and products related to this. 
These books are of course linked to authors with their own role.
A purchase function via the plugin given by the ERP is implemented.


# Installation

## Without ssh key
Using the command :
```
$ git clone https://github.com/basileroutier/esi_lecture_odoo.git
```

## With a ssh key:
```
$ git clone git@github.com:basileroutier/esi_lecture_odoo.git
```


### After the cloning
You need to execute this command (It is better to do it via pycharm) :
	1. Go to repository
	2. Execute command
```
$ python <path_to_odoo-bin> --config <path_to_config_file> --init esi-lecture-rent
```
