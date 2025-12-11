import tkinter as tk
from tkinter import messagebox
import random

class Queue:
    def __init__(self):
        self.item = []
        #self.used_tracking_ids = set()
        
    def generate_id(self):
        return f'{random.randint(100000,999999)}'
    
    def is_empty(self):
        return len(self.item) == 0
    
    def Enqueue(self, items):
        try:
            self.item.append(items)
            print(f'Item "{items}" has been Queued')
            return True
        
        except Exception as e:
            print(f'Error Enqueueing, Details: {e}')
            return False
        
    def Dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        try:
            served_item = self.item.pop(0)
            print(f'Dequeued: {served_item}. Queue Size: {len(self.item)}')
            return served_item
        except IndexError:
            print("Indexing Error - Dequeue Function or Queue is empty")
            return None
        except Exception as e:
            print(f'Dequeueing error: {e}')
            return None
        
    def Peek(self):
        try:
            return self.item[0]
        except IndexError:
            print("Peek Error, Queue is empty")
            return None
        
    def Size(self):
        return len(self.item)
    

            
        
        



