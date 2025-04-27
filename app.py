import streamlit as st

# --- CUSTOM PAGE BACKGROUND ---
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1605296867304-46d5465a13f1");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
# --- END CUSTOM BACKGROUND ---
import streamlit as st

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_fitness_plan(bmi):
    if bmi < 18.5:
        category = "Underweight"
        calories = "2800–3200 per day (84,000–96,000 per month)"
        routine = """- 4x Heavy Strength Training (squats, bench, deadlifts)
- 1x Light Cardio (15–20 min easy cycling or walking)
- 1x Fun Activity (sports, swimming)
- 1x Full Rest"""
        rule = "Eat before bed, lift heavy, nap like a retired cat."
    elif 18.5 <= bmi <= 24.9:
        category = "Normal Weight"
        calories = "2200–2500 per day (66,000–75,000 per month)"
        routine = """- 3x Strength Training (upper, lower, core)
- 2x Moderate Cardio (20–30 min steady pace or easy HIIT)
- 1x Stretching or Mobility Day
- 1x Rest or Light Activity"""
        rule = "You don’t have to kill yourself. You just have to outwork your yesterday."
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
        calories = "1800–2000 per day (54,000–60,000 per month)"
        routine = """- 3x Full-Body Circuit (fast-paced strength + bodyweight exercises)
- 2x HIIT (short, brutal — 15 min max)
- 1x Low-Intensity Long Cardio (walk, cycle — 45 min)
- 1x Active Recovery (yoga or very light walking)"""
        rule = "Short workouts, heavy breathing, constant progress."
    else:
        category = "Obese"
        calories = "1500–1800 per day (45,000–54,000 per month)"
        routine = """- 2x Light Strength (bodyweight squats, band rows, light resistance work)
- 3x Low-Impact Cardio (walking, swimming, cycling — 30 min)
- 1x Stretching or Chair Yoga
- 1x Full Rest"""
        rule = "Move daily — if your joints aren't crying, you're winning."
    
    return category, calories, routine, rule

def main():
    st.title("🏋️ Personalized Fitness Plan Generator")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Fitness_center_logo.png", width=150)
    st.write("Enter your details below to receive your customized monthly fitness plan.")

    weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.1f")
    height = st.number_input("Enter your height (cm)", min_value=30.0, format="%.1f")

    if st.button("Generate Plan"):
        if weight and height:
            bmi = calculate_bmi(weight, height)
            category, calories, routine, rule = get_fitness_plan(bmi)

            st.success(f"**Your BMI is {bmi:.2f} ({category})**")

            st.header("📋 Your Monthly Fitness Plan:")
            st.subheader("🔥 Calories Recommendation")
            st.info(calories)

            st.subheader("🏃 Weekly Workout Routine")
            st.markdown(routine)

            st.subheader("💬 Golden Rule")
            st.warning(rule)
        else:
            st.error("Please enter valid weight and height.")

if __name__ == "__main__":
    main()
