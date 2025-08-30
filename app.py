import streamlit as st
import random

# Page setup
st.set_page_config(
    page_title="Hotel Room Reservation",
    page_icon="🏨",
    layout="wide",   # ensures full width
    initial_sidebar_state="expanded"
)

# Custom CSS for full-width layout
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff; /* light blue background */
    }
    h1 {
        color: #ff5733;
        text-align: center;
        font-size: 42px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 12px 20px;
        width: 100%;  /* make buttons expand */
    }
    .stButton button:hover {
        background-color: #45a049;
        color: yellow;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100%;  /* fit to screen */
    }
    </style>
""", unsafe_allow_html=True)

# Constants
FLOORS = 10
ROOMS_PER_FLOOR = 10
ROOMS_FLOOR_10 = 7
MAX_BOOK = 5

with st.sidebar:
    st.title("🏨 Controls")
    st.info("Manage bookings and hotel status")
    st.warning("Max 5 rooms can be booked at once")

def generate_rooms():
    hotel = []
    for floor in range(1, FLOORS + 1):
        count = ROOMS_FLOOR_10 if floor == 10 else ROOMS_PER_FLOOR
        floor_rooms = []
        for i in range(1, count + 1):
            room_number = floor * 100 + i
            floor_rooms.append({'number': room_number, 'floor': floor, 'booked': False})
        hotel.append(floor_rooms)
    return hotel

def travel_time(room1, room2):
    floor_diff = abs(room1['floor'] - room2['floor'])
    vertical_time = floor_diff * 2
    horiz_time = abs((room1['number'] % 100) - (room2['number'] % 100))
    return vertical_time + horiz_time

def find_best_same_floor(rooms, num_rooms):
    available = [r for r in rooms if not r['booked']]
    if len(available) < num_rooms:
        return None
    best_group = None
    best_time = float('inf')
    for i in range(len(available) - num_rooms + 1):
        group = available[i:i+num_rooms]
        ttime = travel_time(group[0], group[-1])
        if ttime < best_time:
            best_time = ttime
            best_group = group
    return best_group

def find_best_across_floors(hotel, num_rooms):
    all_available = []
    for floor_rooms in hotel:
        for r in floor_rooms:
            if not r['booked']:
                all_available.append(r)
    if len(all_available) < num_rooms:
        return None
    all_available.sort(key=lambda x: (x['floor'], x['number'] % 100))
    best_combo = None
    best_time = float('inf')
    for i in range(len(all_available) - num_rooms + 1):
        combo = all_available[i:i+num_rooms]
        ttime = travel_time(combo[0], combo[-1])
        if ttime < best_time:
            best_time = ttime
            best_combo = combo
    return best_combo

def book_rooms(hotel, num_rooms):
    if num_rooms < 1 or num_rooms > MAX_BOOK:
        return (False, f"Enter number between 1 and {MAX_BOOK}.")
    for floor_rooms in hotel:
        best_group = find_best_same_floor(floor_rooms, num_rooms)
        if best_group:
            for r in best_group:
                r['booked'] = True
            return (True, best_group)
    best_combo = find_best_across_floors(hotel, num_rooms)
    if best_combo:
        for r in best_combo:
            r['booked'] = True
        return (True, best_combo)
    return (False, None)

def main():
    st.markdown("<h1>🏨 Hotel Room Reservation System</h1>", unsafe_allow_html=True)

    if 'hotel' not in st.session_state:
        st.session_state['hotel'] = generate_rooms()

    hotel = st.session_state['hotel']

    col1, col2, col3 = st.columns(3)
    with col1:
        num_rooms = st.number_input(f"Number of rooms to book (max {MAX_BOOK}):", min_value=1, max_value=MAX_BOOK, value=1, step=1)
    with col2:
        if st.button("Book Rooms"):
            success, booked_rooms = book_rooms(hotel, num_rooms)
            if success:
                st.success(f"🎉 Booked rooms: {[r['number'] for r in booked_rooms]} on floors {[r['floor'] for r in booked_rooms]}")
            else:
                st.error("❌ Not enough rooms available.")
    with col3:
        if st.button("Random Occupancy"):
            for floor_rooms in hotel:
                for r in floor_rooms:
                    r['booked'] = (random.random() < 0.3)
            st.rerun()

    if st.button("Reset Bookings"):
        for floor_rooms in hotel:
            for r in floor_rooms:
                r['booked'] = False
        st.rerun()

    st.subheader("Hotel Room Layout")
    for floor_rooms in reversed(hotel):
        cols = st.columns(len(floor_rooms) + 1)
        cols[0].markdown(f"**Floor {floor_rooms[0]['floor']}**")
        for idx, room in enumerate(floor_rooms):
            if room['booked']:
                cols[idx+1].markdown(f"<div style='background-color:#ffcccc; color:#8b0000; text-align:center; padding:6px; border-radius:8px;'>{room['number']}<br>(Booked)</div>", unsafe_allow_html=True)
            else:
                cols[idx+1].markdown(f"<div style='background-color:#e6ffe6; color:#006400; text-align:center; padding:6px; border-radius:8px;'>{room['number']}<br>(Available)</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
