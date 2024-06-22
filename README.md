## BloodEase 🅰️🆎🅱️🅾️
  A Blood Bank Portal.

## Screenshots

### Homepage

 ![Screenshot 2024-06-15 145436](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/19701e65-7c1c-4e58-ab22-a8ac5c0fc7a8)


### Admin Dashboard

 ![Screenshot 2024-06-21 110741](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/2f7187ea-46b6-4c41-83bc-8d78174ba7d3)


### Patient Dashboard
 
![Screenshot 2024-06-22 201425](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/94f306a8-8890-4a29-89c1-a6f6fc583d50)


### Blood Request

 ![Screenshot 2024-06-22 201657](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/7dba6492-be0d-41ad-8fb4-ef1a38c9c5b6)


### User Details

 ![Screenshot 2024-06-21 112145](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/19143079-f7cc-459c-982b-d2c24d67025c)


## Functions

### Admin
- Create an admin account using the following command:
  ```
  python manage.py createsuperuser
  ```
- Upon logging in, admins can view the number of units of each blood group available, the number of donors, the number of blood requests, the number of approved requests, and the total units of blood on the dashboard.
- Admins can view, update, and delete donor information.
- Admins can view, update, and delete patient information.
- Admins can view donation requests made by donors and can approve or reject those requests based on the donor's health status.
- If a donation request is approved by an admin, the donated unit of blood is added to the blood stock of the corresponding blood group.
- If a donation request is rejected by an admin, no units of blood are added to the stock.
- Admins can view blood requests made by patients and can approve or reject those requests.
- If a blood request is approved by an admin, the requested units of blood are deducted from the blood stock of the corresponding blood group.
- If a blood request is rejected by an admin, no units of blood are deducted from the stock.
- Admins can access the history of blood requests.
- Admins can update the unit count of a particular blood group.

### Donor
- Donors can create accounts by providing basic details.
- After logging in, donors can donate blood, and their donations require approval from an admin before the blood is added to the blood stock.
- Donors can view their donation history, including the status of their donations (Pending, Approved, Rejected).
- Donors can see the number of donation requests made, approved, pending, and rejected by an admin on their dashboard.

### Patient
- Patients can create accounts without requiring admin approval.
- After logging in, patients can view the number of blood requests they've made, the number of requests approved, pending, and rejected by an admin on their dashboard.
- Patients can request a required number of units of blood from the blood stock.
- Patients can view their blood request history, including its status (Pending, Approved, Rejected).

## How to Run This Project

- Install Python (3.7.6) (Make sure to select "Add to PATH" during the Python installation).
- Download this project's ZIP folder and extract it.
- Open your terminal and navigate to the project folder. Then run the following commands:

```bash
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py tailwind start
```

- Access the project in your web browser by entering the following URL:

```
http://127.0.0.1:8000/
```

## Feedback

We welcome any suggestions and feedback. Please feel free to reach out to us on LinkedIn.
