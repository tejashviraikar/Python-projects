from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from tkcalendar import Calendar
import datetime

class CalendarApp:
    """Class to create a Calendar Application using Tkinter."""
    
    def __init__(self, root):
        """Initialize the CalendarApp with the main Tkinter window."""
        self.root = root
        self.root.title("Basic Calendar App")
        self.events = {}  # Dictionary to store events
        
        # Calendar widget
        self.cal = Calendar(root, selectmode='day', year=2024, month=1, day=1)
        self.cal.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Event details entry fields
        self.date_var = StringVar()
        self.time_var = StringVar()
        self.desc_var = StringVar()
        
        Label(root, text="Event Date (YYYY-MM-DD):").grid(row=1, column=0)
        self.date_entry = Entry(root, textvariable=self.date_var)
        self.date_entry.grid(row=1, column=1)

        Label(root, text="Event Time (HH:MM AM/PM):").grid(row=2, column=0)
        self.time_entry = Entry(root, textvariable=self.time_var)
        self.time_entry.grid(row=2, column=1)

        Label(root, text="Event Description:").grid(row=3, column=0)
        self.desc_entry = Entry(root, textvariable=self.desc_var)
        self.desc_entry.grid(row=3, column=1)
        
        # Add and Delete buttons
        add_button = Button(root, text="Add Event", command=self.add_event)
        add_button.grid(row=4, column=0, pady=10)

        delete_button = Button(root, text="Delete Event", command=self.delete_event)
        delete_button.grid(row=4, column=1, pady=10)

        view_button = Button(root, text="View Events", command=self.view_events)
        view_button.grid(row=4, column=2, pady=10)

    def add_event(self):
        """Add an event to the calendar."""
        event_date = self.date_var.get()
        event_time = self.time_var.get()
        event_desc = self.desc_var.get()

        # Validate input
        if not event_date or not event_time or not event_desc:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        try:
            datetime.datetime.strptime(event_date, '%Y-%m-%d')
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        # Add event to dictionary
        self.events[(event_date, event_time)] = event_desc
        messagebox.showinfo("Event Added", f"Event '{event_desc}' added on {event_date} at {event_time}.")
        self.clear_inputs()

    def delete_event(self):
        """Delete an event from the calendar."""
        event_date = self.date_var.get()
        event_time = self.time_var.get()

        # Validate input
        if not event_date or not event_time:
            messagebox.showwarning("Input Error", "Event date and time are required for deletion.")
            return

        # Remove event if exists
        if (event_date, event_time) in self.events:
            del self.events[(event_date, event_time)]
            messagebox.showinfo("Event Deleted", f"Event on {event_date} at {event_time} has been deleted.")
        else:
            messagebox.showwarning("Event Not Found", "No event found for the given date and time.")
        self.clear_inputs()

    def view_events(self):
        """View all events on the calendar."""
        events_list = "\n".join([f"{date} at {time}: {desc}" for (date, time), desc in self.events.items()])
        if events_list:
            messagebox.showinfo("All Events", events_list)
        else:
            messagebox.showinfo("No Events", "No events found.")

    def clear_inputs(self):
        """Clear the input fields."""
        self.date_var.set("")
        self.time_var.set("")
        self.desc_var.set("")

# Run the Tkinter calendar application
root = Tk()
app = CalendarApp(root)
root.mainloop() 
