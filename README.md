# 🏨 Hotel Booking Optimizer

An interactive **Streamlit web app** for optimizing hotel room reservations.
It allows booking multiple rooms at once (up to 5), automatically groups rooms close together, and visualizes booked vs. available rooms with color-coded UI.

---

## 🚀 Live Demo

👉 Try the app here: [Hotel Booking Optimizer Live](https://hotel-booking-optimizergit-dq5dnrhxwd8lznzgzxnddx.streamlit.app/)

---

## ✨ Features

* 📌 **Book up to 5 rooms** in one click
* 🎨 **Color-coded layout** (Booked = 🔴 Red, Available = 🟢 Green)
* 🎲 **Random Occupancy** button to simulate bookings
* 🔄 **Reset Bookings** button to clear all reservations
* 🏢 Handles **10 floors** (with 10 rooms each, floor 10 has 7 rooms)
* ⚡ Optimizes grouping so guests get rooms **close to each other**

---

## 🖼️ Demo Screenshot

(Add your screenshot here once you take one, e.g.)

![<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ae1274c6-1c63-4194-96da-236e57c992a2" />
](screenshot.png)

---

## 🛠️ Tech Stack

* **Python 3.12**
* **Streamlit 1.49.1**

---

## ⚙️ How It Works

1. **Room Availability**

   * Each floor has rooms numbered like `101, 102, …, 110` (except floor 10 which has 7 rooms).
   * A room can either be **Available (🟢 Green)** or **Booked (🔴 Red)**.

2. **Booking Algorithm**

   * User requests **1–5 rooms**.
   * The system first checks if the requested rooms are available **on the same floor** in sequence.
   * If found → those rooms are booked.
   * If not → it searches across multiple floors and books the **closest set of rooms** (minimizing walking/travel distance).

3. **Travel Time Calculation**

   * Vertical movement = `2 units per floor difference`.
   * Horizontal movement = `difference in room positions on the floor`.
   * Rooms are grouped to minimize this combined travel time.

4. **Controls**

   * **Book Rooms** → Books the optimal group.
   * **Random Occupancy** → Marks \~30% of rooms as booked randomly.
   * **Reset Bookings** → Clears all reservations.

---

## 📂 Project Structure

```
hotel-booking-optimizer/
│── app.py              # Main Streamlit app
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

---

## ⚙️ Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/divitisanthoshi/hotel-booking-optimizer.git
   cd hotel-booking-optimizer
   ```

2. Create virtual environment (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📜 License

This project is licensed under the MIT License.

---
