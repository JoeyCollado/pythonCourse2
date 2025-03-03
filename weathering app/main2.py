import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
from PIL import Image, ImageTk

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = '0c9f0ad88ca1f29fe716dae44341b0df'

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weathering System App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Set up frames
        self.top_frame = ttk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        # City Entry
        self.city_entry = ttk.Entry(self.top_frame, font=("Helvetica", 16))
        self.city_entry.pack(pady=50)
        
        # Submit Button
        self.submit_button = ttk.Button(self.top_frame, text="Get Weather", command=self.update_weather)
        self.submit_button.pack(pady=10)
        
        # Date and Time Label
        self.datetime_label = ttk.Label(self.top_frame, text="", font=("Helvetica", 16))
        self.datetime_label.pack(pady=10)
        
        # Weather Information Label
        self.weather_label = ttk.Label(self.bottom_frame, text="", font=("Helvetica", 16))
        self.weather_label.pack(pady=10)
        
        # Weather Icon
        self.weather_icon_label = ttk.Label(self.bottom_frame)
        self.weather_icon_label.pack(pady=10)
        
        # Update the time
        self.update_time()
    
    def update_time(self):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label.config(text=f"Current Date and Time: {current_time}")
        self.root.after(1000, self.update_time)
    
    def update_weather(self):
        city = self.city_entry.get()
        if not city:
            self.weather_label.config(text="Please enter a city name.")
            return
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            
            sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
            sunset = datetime.fromtimestamp(data['sys']['sunset'])
            now = datetime.now()
            is_daytime = sunrise < now < sunset
            
            weather_info = f"Weather: {weather.capitalize()}\nTemperature: {temp}°C\nHumidity: {humidity}%\n{'Daytime' if is_daytime else 'Nighttime'}"
            self.weather_label.config(text=weather_info)
            
            # Update weather icon
            icon = self.get_weather_icon(weather, is_daytime)
            if icon:
                self.weather_icon_label.config(image=icon)
                self.weather_icon_label.image = icon
        else:
            error_message = response.json().get('message', 'Unknown error')
            self.weather_label.config(text=f"Failed to retrieve weather data:")
            print(f"Failed to retrieve weather data: {response.status_code}")
    
    def get_weather_icon(self, weather_description, is_daytime):
        if 'cloud' in weather_description:
            icon_path = 'C:\\Users\\akosi\\OneDrive\\Desktop\\cloud.png'
            
        elif 'clear' in weather_description:
            icon_path = 'C:\\Users\\akosi\\OneDrive\\Desktop\\sunny.png' if is_daytime else 'C:\\Users\\akosi\\OneDrive\\Desktop\\moon.png'
            
        elif 'rain' in weather_description:
            icon_path = 'C:\\Users\\akosi\\OneDrive\\Desktop\\rain.png'
            
        elif 'snow' in weather_description:
            icon_path = 'C:\\Users\\akosi\\OneDrive\\Desktop\\snow.png'
            
        else:
            icon_path = None
        
        if icon_path:
            icon_image = Image.open(icon_path)
            icon_image = icon_image.resize((250, 150), Image.LANCZOS)
            return ImageTk.PhotoImage(icon_image)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
