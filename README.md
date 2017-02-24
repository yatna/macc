#Mobile App Control Center (MACC)
MACC is a backend platform for the Peace Corps mobile applications - Malaria and FirstAide. The Mobile App Control Center allows the volunteers at Peace Corps HQ to send or edit any information in their mobile applications through a set of APIs.

If you already had the server installed, it is advised that you delete the current database to remove errors related to the model fields updates. this can be done by running the following command:

    `python manage.py flush`

#On Malaria App
MACC works on Malaria Prevention application as infoHub, a portal where posts can be added and notified to the mobile app users(volunteers). Posts on infoHub mainly focus on malaria prevention tips and malaria awareness.

#On FirstAide App
MACC works on PCSA mobile and web apps, MACC makes the mobile apps fully dynamic and all the information present in the mobile apps is fetched from MACC through APIs.


Installation Guide - [here](https://github.com/systers/macc/blob/develop/docs/Installation%20Guide.md)
API Documentation -  [here](https://docs.google.com/document/d/1uQ42HQGIEOWoD-PtRRGoKLN15S-EhEkWgsIxiceNMGI/edit?usp=sharing)
Contribution Guide = [here](https://github.com/systers/macc/blob/develop/docs/Contribution.md)
