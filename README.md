BloodEase 🅰️🆎🅱️🅾️

## Screenshots

### Homepage

![Homepage] ![Screenshot 2023-11-08 231423](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/f6fcddbd-9cdd-435d-a0d8-492d60097266)


### Admin Dashboard

![Admin Dashboard] ![Screenshot 2023-11-08 231404](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/5e8ede8b-3cf6-4045-94b6-dd6e7bfe5e1f)


### Blood Donation

![Blood Donation] ![Screenshot 2023-11-08 235615](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/f289f178-1b34-4ff6-ae1b-60a8ca07763f)


### Blood Request

![Blood Request] ![Screenshot 2023-11-08 222610](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/04a32f77-3b23-4f21-85c0-12b3241433e1)


### User Details

![User] ![Screenshot 2023-11-09 172226](https://github.com/Mohd-Daniyal/BloodEase/assets/96229438/e349e6fa-9fe3-43ac-ae7e-b92c2769f391)


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
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

- Access the project in your web browser by entering the following URL:

```
http://127.0.0.1:8000/
```

## Feedback

We welcome any suggestions and feedback. Please feel free to reach out to us on LinkedIn.
