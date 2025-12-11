import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random

# ==============================================================================
# BACKEND DATA STRUCTURES (from Connected_Structures)
# ==============================================================================

class Item:
    """Node for Item linked list within a Container."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Container:
    """Node for Container linked list within Storage. Holds a list of Items."""
    def __init__(self):
        self.items = None
        self.next = None
        self.max_items = 10
        self.item_count = 0

    def is_empty(self):
        return self.items is None
    
    def is_full(self):
        return self.item_count == self.max_items
    
    def order_item(self, data):
        if self.is_full():
            return
        
        new_item = Item(data)
        if self.is_empty():
            self.items = new_item
        else:
            current_item = self.items
            while current_item.next:
                current_item = current_item.next
            current_item.next = new_item
        self.item_count += 1

    def ship_item(self):
        if self.is_empty():
            return None
        
        shipped_item_data = self.items.data
        self.items = self.items.next # Move head pointer
        self.item_count -= 1
        return shipped_item_data


class Storage:
    """Linked list of Containers."""
    def __init__(self):
        self.containers = None
        self.max_containers = 10
        self.container_count = 0

    
    # Keeping the methods required for potential future integration:
    
    def is_empty(self):
        return self.containers is None
    
    def add_container(self):
        if self.is_empty():
            self.containers = Container()
            self.container_count += 1
            return

        current_container = self.containers
        while current_container.next:
            current_container = current_container.next
        current_container.next = Container()
        self.container_count += 1
        
    def select_recent_container(self):
        if self.is_empty():
            return None
        
        current_container = self.containers
        while current_container and current_container.next:
            current_container = current_container.next
        return current_container

    def add_item(self, data):
        if self.container_count == 0 or self.select_recent_container().is_full():
            if self.container_count < self.max_containers:
                 self.add_container()
            else:
                #print("Storage is full.")
                return

        selected_container = self.select_recent_container()
        if selected_container:
            selected_container.order_item(data)


class OrderQueue:
    """FIFO Queue for incoming orders, handles unique ID generation."""
    # Order Queue Implementation
    def __init__(self):
        self.item = []
        # CRUCIAL ADDITION: Set to ensure tracking IDs are never reused - as per Ceriola
        self.used_tracking_ids = set() 
    #For Simulation - Random Int    
    def generate_unique_id(self):
        """Generates a unique 6-digit tracking ID by checking the used_tracking_ids set."""
        tracking_id = None
        max_attempts = 100
        attempts = 0
        while tracking_id is None or tracking_id in self.used_tracking_ids:
            if attempts >= max_attempts:
                raise Exception("Failed to generate a unique tracking ID.") 
            tracking_id = f'{random.randint(100000, 999999)}'
            attempts += 1
        return tracking_id
    
    def is_empty(self):
        return len(self.item) == 0
    
    def enqueue(self, item_data):
        # item_data is expected to be a dictionary: {'name', 'address', 'tracking_id'}
        try:
            self.item.append(item_data)
            self.used_tracking_ids.add(item_data['tracking_id']) # Record the used ID
            #print(f"Item '{item_data.get('name')}' (ID: {item_data.get('tracking_id')}) has been Queued.")
            return True
        except Exception as e:
            #print(f'Error Enqueueing, Details: {e}')
            return False
        
    def dequeue(self):
        if self.is_empty():
            return None
        try:
            served_item = self.item.pop(0)
            #print(f"Dequeued: {served_item.get('name')} | Tracking ID: {served_item.get('tracking_id')}. Queue Size: {len(self.item)}")
            return served_item
        except Exception as e:
            #print(f'Dequeueing error: {e}')
            return None
    
    def peek(self):
        if self.is_empty():
            return None
        return self.item[0]
        
    def size(self):
        return len(self.item)


class ShippingQueue:
    """Standard FIFO Queue for items ready to be shipped."""
    def __init__(self):
        self.queue = []


    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            #print("Shipping is currently empty. Dequeueing is not possible.")
            return None
        return self.queue.pop(0)


class Logs:
    """Fixed-size stack implementation for activity logs."""
    def __init__(self): 
        self.logs_stack = []
        self.log_capacity = 20 #variable
        self.top = -1
    
    def log_amount(self):
        return len(self.logs_stack)
        #For terminal only, for checking lang
    def log_full(self):
        return self.top == self.log_capacity - 1 
    
    def new_log(self, current_log):
        """Pushes a new log entry onto the stack."""
        if self.log_full():
            # If full, remove the oldest log (bottom of stack)
            self.logs_stack.pop(0) 
            self.top -= 1
            #print("Log full, removed oldest entry.") - also a stack implementation
        
        self.logs_stack.append(current_log)
        self.top += 1 
        #print(f"Added new log: {current_log}")
    
    def remove_log(self):
        """Pops the most recent log entry."""
        if self.top == -1:
            return None
        current_log = self.logs_stack.pop()
        self.top -= 1 
        return current_log
    
# ===============================================================================================
# TKINTER UI APPLICATION (from Miguel Magbanua, connected to backend) - very long line of code
# ===============================================================================================

class ItemManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Item Manager")
        self.root.geometry("950x600")
        self.root.minsize(700, 450)
        self.root.resizable(False, False)
        
        # Backend Instances
        self.order_queue = OrderQueue() # Used for unique ID generation - the randint function from before
        self.backend_logs = Logs()      # Used for logging - logs storage
        self.storage = Storage()        # Conceptual storage 
        
        # UI Data structures
        self.items = [] # list of (item_data_dict, container_widget, boolean_var)
        self.pending_items = [] # list of (item_data_dict, frame_widget)
        self.to_remove = [] # list of (item_data_dict, container_widget, boolean_var)
        
        # --- Constants and Styling --- (variables, for easy implementation and uniform coloring po)
        PRIMARY_ACCENT = "#30A0E0" 
        SECONDARY_ACCENT = "#E8D3A5"
        WINDOW_BG = "#FFE3B3"      
        DARK_TEXT_COLOR = "#006BBB"      
        LIGHT_TEXT_COLOR = "white"      
        BUTTON_TEXT_COLOR = LIGHT_TEXT_COLOR 
        
        FONT_FAMILY = "Verdana"
        BASE_FONT = (FONT_FAMILY, 9)
        TITLE_FONT = (FONT_FAMILY, 9, 'bold')

        self.root.config(bg=WINDOW_BG)
        
        style = ttk.Style()
        style.theme_use('clam') 
        
        style.configure('TFrame', background=WINDOW_BG)
        style.configure('TLabel', background=WINDOW_BG, font=BASE_FONT, foreground=DARK_TEXT_COLOR)

        # Apply basic styling for this combined code
        style.configure('TLabelframe', background=WINDOW_BG)     
        style.configure('White.TFrame', background='white')
        style.configure('DarkOnWhite.TLabel', background='white', foreground=DARK_TEXT_COLOR, font=BASE_FONT)
        style.configure('TLabelframe.Label', background=WINDOW_BG, foreground=DARK_TEXT_COLOR, font=TITLE_FONT, padding=(5, 0, 5, 0))
        style.configure('TEntry', fieldbackground='white', foreground=DARK_TEXT_COLOR, font=BASE_FONT, bordercolor=SECONDARY_ACCENT, selectbackground=SECONDARY_ACCENT)
        style.configure('Primary.TButton', background=PRIMARY_ACCENT, foreground=BUTTON_TEXT_COLOR, font=TITLE_FONT, padding=[4, 2, 4, 2], relief='flat', borderwidth=0)
        style.map('Primary.TButton', background=[('active', SECONDARY_ACCENT)], foreground=[('active', DARK_TEXT_COLOR)])
        try:
            self.root.tk.call("ttk::style", "configure", 'Primary.TButton', "-borderradius", 30)
        except Exception:
            pass
        root.option_add('*TCombobox*Listbox.font', BASE_FONT)
        root.option_add('*TCombobox*Listbox.selectBackground', SECONDARY_ACCENT) 
        root.option_add('*TCombobox*Listbox.Background', 'white')
        style.configure('TCombobox', fieldbackground='white', background=PRIMARY_ACCENT, foreground=DARK_TEXT_COLOR, font=BASE_FONT, padding=3)
        style.configure('Treeview', font=BASE_FONT, rowheight=24, background='white', fieldbackground='white', foreground=DARK_TEXT_COLOR)
        style.map('Treeview', background=[('selected', SECONDARY_ACCENT)])
        style.configure('Treeview.Heading', font=TITLE_FONT, background=PRIMARY_ACCENT, foreground=LIGHT_TEXT_COLOR, padding=(5, 5))
        
        self.root.columnconfigure(0, weight=3) 
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.log_window = None 
        self.log_tree = None

        # --- Items Frame (Left Panel) ---
        items_frame = ttk.LabelFrame(root, text="Items", padding=10)
        items_frame.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
        items_frame.columnconfigure(0, weight=1)
        items_frame.rowconfigure(1, weight=1) 

        # Search Bar
        search_frame = ttk.Frame(items_frame)
        search_frame.grid(row=0, column=0, columnspan=2, sticky="EW", pady=5) 
        search_frame.columnconfigure(0, weight=10) 
        search_frame.columnconfigure(1, weight=1) 
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, style='TEntry') 
        self.search_entry.grid(row=0, column=0, padx=3, sticky="EW")

        self.filter_var = tk.StringVar(value="Item name")
        self.filter_menu = ttk.Combobox(search_frame, textvariable=self.filter_var, values=["Item name", "Tracking number"], state="readonly")
        self.filter_menu.grid(row=0, column=1, padx=3, sticky="EW")

        self.search_button = ttk.Button(search_frame, text="Search", command=self.apply_search, style='Primary.TButton')
        self.search_button.grid(row=0, column=2, padx=3)
        self.show_all_button = ttk.Button(search_frame, text="Show All", command=self.show_all_items, style='Primary.TButton')
        self.show_all_button.grid(row=0, column=3, padx=5)

        # Scrollable Item Display Area
        self.items_canvas = tk.Canvas(items_frame, bg='white', highlightthickness=0)
        self.items_scrollbar = ttk.Scrollbar(items_frame, orient="vertical", command=self.items_canvas.yview)
        self.items_scrollable_frame = ttk.Frame(self.items_canvas, style='White.TFrame')
        self.items_scrollable_frame.bind("<Configure>", lambda e: self.items_canvas.configure(scrollregion=self.items_canvas.bbox("all"), width=self.items_scrollable_frame.winfo_width()))
        self.items_canvas.create_window((0, 0), window=self.items_scrollable_frame, anchor="nw")
        self.items_canvas.configure(yscrollcommand=self.items_scrollbar.set)
        
        self.items_canvas.grid(row=1, column=0, sticky="NSEW")
        self.items_scrollbar.grid(row=1, column=1, sticky="NS")

        # --- Right Panel ---
        right_frame = ttk.Frame(root, padding=5)
        right_frame.grid(row=0, column=1, sticky="NSEW")
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=2)
        right_frame.rowconfigure(1, weight=2)

        # --- Adding Items Frame ---
        add_frame = ttk.LabelFrame(right_frame, text="Adding Items", padding=5)
        add_frame.grid(row=0, column=0, sticky="NSEW", pady=5)
        add_frame.columnconfigure(0, weight=1)
        add_frame.rowconfigure(1, weight=1)

        self.add_button = ttk.Button(add_frame, text="+ Add", command=self.open_add_form, style='Primary.TButton')
        self.add_button.grid(row=0, column=0, sticky="W", padx=5, pady=2) 

        self.pending_canvas = tk.Canvas(add_frame, bg='white', highlightthickness=0)
        self.pending_scrollbar = ttk.Scrollbar(add_frame, orient="vertical", command=self.pending_canvas.yview)
        self.pending_frame = ttk.Frame(self.pending_canvas, style='White.TFrame')
        self.pending_frame.bind("<Configure>", lambda e: self.pending_canvas.configure(scrollregion=self.pending_canvas.bbox("all"), width=self.pending_frame.winfo_width()))
        self.pending_canvas.create_window((0, 0), window=self.pending_frame, anchor="nw")
        self.pending_canvas.configure(yscrollcommand=self.pending_scrollbar.set)
        self.pending_canvas.grid(row=1, column=0, sticky="NSEW")
        self.pending_scrollbar.grid(row=1, column=1, sticky="NS")

        self.confirm_add_button = ttk.Button(add_frame, text="Confirm", command=self.confirm_items, style='Primary.TButton')
        self.confirm_add_button.grid(row=2, column=0, sticky="W", padx=5, pady=2) 

        # --- Removing Items Frame ---
        remove_frame = ttk.LabelFrame(right_frame, text="Removing Items", padding=5)
        remove_frame.grid(row=1, column=0, sticky="NSEW", pady=5)
        remove_frame.columnconfigure(0, weight=1)
        remove_frame.rowconfigure(1, weight=1)

        self.remove_button = ttk.Button(remove_frame, text="- Remove", command=self.preview_removal, style='Primary.TButton')
        self.remove_button.grid(row=0, column=0, sticky="W", padx=5, pady=2) 

        self.removal_canvas = tk.Canvas(remove_frame, bg='white', highlightthickness=0)
        self.removal_scrollbar = ttk.Scrollbar(remove_frame, orient="vertical", command=self.removal_canvas.yview)
        self.removal_scrollable_frame = ttk.Frame(self.removal_canvas, style='White.TFrame')
        self.removal_scrollable_frame.bind("<Configure>", lambda e: self.removal_canvas.configure(scrollregion=self.removal_scrollable_frame.bbox("all"), width=self.removal_scrollable_frame.winfo_width()))
        self.removal_canvas.create_window((0, 0), window=self.removal_scrollable_frame, anchor="nw")
        self.removal_canvas.configure(yscrollcommand=self.removal_scrollbar.set)
        self.removal_canvas.grid(row=1, column=0, sticky="NSEW")
        self.removal_scrollbar.grid(row=1, column=1, sticky="NS")

        button_row = ttk.Frame(remove_frame)
        button_row.grid(row=2, column=0, columnspan=2, sticky="EW", padx=5, pady=2)
        
        self.select_all_button = ttk.Button(button_row, text="Select All", command=self.select_all_removals, style='Primary.TButton')
        self.select_all_button.pack(side="left", padx=5)
        
        self.recall_button = ttk.Button(button_row, text="Recall", command=self.recall_items, style='Primary.TButton')
        self.recall_button.pack(side="left", padx=5)
        
        self.recall_confirm_button = ttk.Button(button_row, text="Confirm", command=self.confirm_removal, style='Primary.TButton')
        self.recall_confirm_button.pack(side="left", padx=5)

        self.logs_button = ttk.Button(button_row, text="Logs", command=self.show_logs, style='Primary.TButton')
        self.logs_button.pack(side="right", padx=5)

    def placeholder_action(*args):
        """A placeholder function for button commands that are not yet fully implemented in the backend."""
        #print("Action placeholder triggered.")
        pass

    # --- UI METHODS CONNECTED TO BACKEND --- by Moya

    def log_action(self, action, item_name, tracking):
        """Logs an action using the backend Logs stack."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Log is stored as a dictionary, which is then handled by the Logs stack
        log_entry = {
            "timestamp": timestamp,
            "action": action,
            "item": item_name,
            "tracking": tracking
        }
        self.backend_logs.new_log(log_entry)

    def show_logs(self):
        """Opens and initializes the log viewing window."""
        if self.log_window is not None and self.log_window.winfo_exists():
            self.log_window.lift()
            self.log_window.focus_force()
            return 

        self.log_window = tk.Toplevel(self.root)
        self.log_window.title("Activity Logs")
        self.log_window.geometry("800x450")
        
        # ... (Filter Frame setup) ... VERY IMPORTANT
        filter_frame = ttk.Frame(self.log_window)
        filter_frame.pack(fill="x", padx=10, pady=10)
        self.log_search_var = tk.StringVar()
        log_entry = ttk.Entry(filter_frame, textvariable=self.log_search_var, width=25, style='TEntry')
        log_entry.pack(side="left", padx=5)
        self.log_filter_var = tk.StringVar(value="Item Name")
        log_combobox = ttk.Combobox(filter_frame, textvariable=self.log_filter_var, values=["Time", "Item Name", "Action", "Tracking number"], state="readonly", width=15, style='TCombobox')
        log_combobox.pack(side="left", padx=5)
        ttk.Button(filter_frame, text="Search", command=self.apply_log_search, style='Primary.TButton').pack(side="left", padx=5)
        ttk.Button(filter_frame, text="Show All", command=self.show_all_logs, style='Primary.TButton').pack(side="left", padx=5)

        columns = ("timestamp", "action", "item", "tracking")
        self.log_tree = ttk.Treeview(self.log_window, columns=columns, show="headings")
        self.log_tree.heading("timestamp", text="Time")
        self.log_tree.heading("action", text="Action")
        self.log_tree.heading("item", text="Item Name")
        self.log_tree.heading("tracking", text="Tracking #")
        
        self.log_tree.column("timestamp", width=130)
        self.log_tree.column("action", width=80)
        self.log_tree.column("item", width=250)
        self.log_tree.column("tracking", width=150)
        
        scrollbar = ttk.Scrollbar(self.log_window, orient="vertical", command=self.log_tree.yview)
        self.log_tree.configure(yscrollcommand=scrollbar.set)
        
        self.log_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.show_all_logs()

    def apply_log_search(self):
        """Filters the displayed logs based on user input."""
        query = self.log_search_var.get().strip().lower()
        filter_type = self.log_filter_var.get()
        
        for item in self.log_tree.get_children():
            self.log_tree.delete(item)

        # Read logs from the backend stack
        # Convert dictionary logs to tuples for Treeview display and sorting (Filtering System)
        log_data = [(l['timestamp'], l['action'], l['item'], l['tracking']) for l in self.backend_logs.logs_stack]
        sorted_logs = sorted(log_data, key=lambda x: datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"), reverse=True) 

        for log in sorted_logs:
            timestamp, action, item_name, tracking = log
            match = False
            
            if filter_type == "Time" and query in timestamp.lower():
                match = True
            elif filter_type == "Item Name" and query in item_name.lower():
                match = True
            elif filter_type == "Action" and query in action.lower():
                match = True
            elif filter_type == "Tracking number" and query in tracking.lower():
                match = True
            
            # Show if there's a match or if the search query is empty
            if match or query == "":
                self.log_tree.insert("", "end", values=log)

    def show_all_logs(self):
        """Clears search and displays all logs, sorted by time."""
        if not self.log_tree:
            return
            
        self.log_search_var.set("")
        for item in self.log_tree.get_children():
            self.log_tree.delete(item)
            
        # Read logs from the backend stack
        log_data = [(l['timestamp'], l['action'], l['item'], l['tracking']) for l in self.backend_logs.logs_stack]
        sorted_logs = sorted(log_data, key=lambda x: datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"), reverse=True) 
        
        for log in sorted_logs:
            self.log_tree.insert("", "end", values=log)

    # --- UI INTERACTION METHODS ---
    # Add Button - New Window
    def open_add_form(self):
        """Opens a popup form for adding a new item."""
        popup = tk.Toplevel(self.root)
        popup.title("Item details")
        popup.geometry("450x250") # Adjusted size for address field
        popup.transient(self.root)
        popup.grab_set()

        popup.grid_columnconfigure(1, weight=1)

        ttk.Label(popup, text="Item name").grid(row=0, column=0, padx=15, pady=5, sticky="W")
        name_entry = ttk.Entry(popup, style='TEntry')
        name_entry.grid(row=0, column=1, padx=15, pady=5, sticky="EW")
        
        ttk.Label(popup, text="Address").grid(row=1, column=0, padx=15, pady=5, sticky="W")
        address_entry = ttk.Entry(popup, style='TEntry')
        address_entry.grid(row=1, column=1, padx=15, pady=5, sticky="EW")

        ttk.Label(popup, text="Tracking number").grid(row=2, column=0, padx=15, pady=5, sticky="W")
        # Tracking number is generated automatically and shown
        try:
            unique_id = self.order_queue.generate_unique_id()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate unique ID: {e}")
            popup.destroy()
            return

        tracking_var = tk.StringVar(value=unique_id)
        tracking_label = ttk.Label(popup, textvariable=tracking_var, style='DarkOnWhite.TLabel')
        tracking_label.grid(row=2, column=1, padx=15, pady=5, sticky="EW")
        # Secondary window for adding
        def add_pending():
            name = name_entry.get().strip()
            address = address_entry.get().strip()
            tracking = tracking_var.get()

            if not name or not address:
                messagebox.showerror("Input Error", "Name and Address cannot be empty.")
                return

            new_item_data = {
                'name': name,
                'address': address,
                'tracking_id': tracking
            }
            
            # Add to pending list and update UI
            frame = self.create_pending_widget(new_item_data)
            self.pending_items.append((new_item_data, frame))
            popup.destroy()

        ttk.Button(popup, text="Add to Pending", command=add_pending, style='Primary.TButton').grid(row=3, column=0, columnspan=2, pady=10)
        name_entry.focus_set()

    def create_pending_widget(self, item_data):
        """Helper to create and display a widget in the pending frame."""
        frame = ttk.Frame(self.pending_frame, style='White.TFrame')
        frame.pack(fill="x", padx=4, pady=4)
        
        TITLE_FONT = ("Verdana", 9, 'bold')
        SMALL_FONT = ("Verdana", 8)
        
        ttk.Label(frame, text=f"Item: {item_data['name']}", font=TITLE_FONT, style='DarkOnWhite.TLabel').grid(row=0, column=0, sticky="W")
        ttk.Label(frame, text=f"ID: {item_data['tracking_id']}", font=SMALL_FONT, style='DarkOnWhite.TLabel').grid(row=1, column=0, sticky="W")
        ttk.Button(frame, text="X", command=lambda: self.remove_pending(frame), style='Primary.TButton').grid(row=0, column=1, rowspan=2, padx=4, sticky="E")
        frame.grid_columnconfigure(0, weight=1)
        ttk.Separator(frame, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="EW", pady=4)
        return frame

    def remove_pending(self, frame):
        """Removes a widget from the pending list."""
        for i, (_, f) in enumerate(self.pending_items):
            if f == frame:
                f.destroy()
                del self.pending_items[i]
                break

    def create_item_widget(self, item_data, container):
        """Helper to create and display a widget in the main items frame."""
        var = tk.BooleanVar()
        
        TITLE_FONT = ("Verdana", 9, 'bold')
        SMALL_FONT = ("Verdana", 8)
        
        text_name = ttk.Label(container, text=f"Item name: {item_data['name']}", font=TITLE_FONT, style='DarkOnWhite.TLabel')
        text_track = ttk.Label(container, text=f"Tracking number: {item_data['tracking_id']}", font=SMALL_FONT, style='DarkOnWhite.TLabel')
        cb = ttk.Checkbutton(container, variable=var)
        
        cb.grid(row=0, column=0, padx=4, sticky="N")
        text_name.grid(row=0, column=1, sticky="W")
        text_track.grid(row=1, column=1, sticky="W")
        ttk.Separator(container, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="EW", pady=4)
        
        return container, var

    def confirm_items(self):
        """Moves all pending items to the main storage list and logs the action."""
        for item_data, frame in list(self.pending_items):
            
            # 1. Enqueue item to OrderQueue (ensures ID is recorded as used)
            self.order_queue.enqueue(item_data)
            
            # 2. Update UI list (self.items) and display
            container = ttk.Frame(self.items_scrollable_frame, style='White.TFrame')
            container, var = self.create_item_widget(item_data, container)
            container.pack(fill="x", padx=4, pady=4)
            self.items.append((item_data, container, var))
            
            # 3. Log action
            self.log_action("Added", item_data['name'], item_data['tracking_id'])
            
            # 4. Remove from pending area
            frame.destroy()
            
        self.pending_items.clear()
        messagebox.showinfo("Confirmation", f"Successfully confirmed {len(self.items)} items.")


    def preview_removal(self):
        """Moves selected items from the main list to the removal preview list."""
        new_removals = []
        remaining_items = []
        
        for item in self.items:
            item_data, container, var = item
            if var.get():
                container.pack_forget()
                
                # Create removal preview widget
                rem_container = ttk.Frame(self.removal_scrollable_frame, style='White.TFrame')
                rem_var = tk.BooleanVar(value=True) # Default to selected for removal
                rem_cb = ttk.Checkbutton(rem_container, variable=rem_var)
                rem_cb.grid(row=0, column=0, padx=4, sticky="N")
                
                TITLE_FONT = ("Verdana", 9, 'bold')
                SMALL_FONT = ("Verdana", 8)
                
                ttk.Label(rem_container, text=f"Item name: {item_data['name']}", font=TITLE_FONT, style='DarkOnWhite.TLabel').grid(row=0, column=1, sticky="W")
                ttk.Label(rem_container, text=f"Tracking number: {item_data['tracking_id']}", font=SMALL_FONT, style='DarkOnWhite.TLabel').grid(row=1, column=1, sticky="W")
                ttk.Separator(rem_container, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="EW", pady=4)
                rem_container.pack(fill="x", padx=4, pady=4)
                
                new_removals.append((item_data, rem_container, rem_var))
            else:
                remaining_items.append(item)
                
        self.items = remaining_items
        self.to_remove.extend(new_removals)

    def select_all_removals(self):
        """Selects all items in the removal preview list."""
        for _, _, var in self.to_remove:
            var.set(True)

    def recall_items(self):
        """Recalls selected items from the removal preview back to the main list."""
        keep_removals = []
        for item in self.to_remove:
            item_data, rem_container, rem_var = item
            if rem_var.get():
                # Item is selected for recall
                rem_container.destroy()
                
                # Add back to main item list UI
                container = ttk.Frame(self.items_scrollable_frame, style='White.TFrame')
                container, var = self.create_item_widget(item_data, container)
                container.pack(fill="x", padx=4, pady=4)
                self.items.append((item_data, container, var))
                
                self.log_action("Recalled", item_data['name'], item_data['tracking_id'])
            else:
                # Item remains in the removal list
                keep_removals.append(item)
                
        self.to_remove = keep_removals

    def confirm_removal(self):
        """Permanently removes all selected items from the removal preview list and logs the action."""
        keep_removals = []
        for item in self.to_remove:
            item_data, rem_container, rem_var = item
            if rem_var.get():
                # Item is confirmed for removal
                rem_container.destroy()
                self.log_action("Removed", item_data['name'], item_data['tracking_id'])
            else:
                # Item is recalled by deselecting it in the preview
                keep_removals.append(item)
                
        self.to_remove = keep_removals

    def apply_search(self):
        """Filters the items displayed in the main list based on search query."""
        query = self.search_var.get().strip().lower()
        filter_by = self.filter_var.get()

        for item_data, container, var in self.items:
            match = False
            
            # Note: item_data is a dictionary {'name', 'address', 'tracking_id'}
            if filter_by == "Item name" and query in item_data['name'].lower():
                match = True
            elif filter_by == "Tracking number" and query in item_data['tracking_id'].lower():
                match = True

            if match or query == "":
                container.pack(fill="x", padx=4, pady=4)
            else:
                container.pack_forget()

    def show_all_items(self):
        """Clears the search filter and shows all items."""
        self.search_var.set("") 
        self.apply_search() 


# --- Main Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ItemManagerApp(root)
    
    # Example of logging some data manually for testing the Logs window
    # The log action now records to the backend Logs stack.
    # We can check this exists if we open Logs Directly
    app.log_action("App Init", "System Check", "000000")
    
    root.mainloop()