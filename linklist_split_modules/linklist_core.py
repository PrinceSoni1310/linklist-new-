# Auto-generated module (part 1)
import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx
import io
from PIL import Image
import sys
from io import StringIO
import contextlib
import pandas as pd
import time
import random
import math

try:
    from quiz_config import QUIZ_QUESTIONS
except ImportError:
    # Fallback quiz data if import fails
    QUIZ_QUESTIONS = []

# Fallback data for coding challenges and time challenges
CODING_CHALLENGES = [
    {
        "title": "Reverse a Linked List",
        "difficulty": "easy",
        "points": 50,
        "description": "Write a function to reverse a singly linked list.",
        "starter_code": "def reverse_linked_list(head):\n    # Your code here\n    pass",
        "solution": "def reverse_linked_list(head):\n    prev = None\n    current = head\n    while current:\n        next_node = current.next\n        current.next = prev\n        prev = current\n        current = next_node\n    return prev",
        "test_cases": [{"input": "[1,2,3,4,5]", "expected": "[5,4,3,2,1]"}]
    },
    {
        "title": "Detect Cycle in Linked List",
        "difficulty": "medium",
        "points": 75,
        "description": "Determine if a linked list has a cycle using Floyd's algorithm.",
        "starter_code": "def has_cycle(head):\n    # Your code here\n    pass",
        "solution": "def has_cycle(head):\n    if not head or not head.next:\n        return False\n    slow = head\n    fast = head.next\n    while fast and fast.next:\n        if slow == fast:\n            return True\n        slow = slow.next\n        fast = fast.next.next\n    return False",
        "test_cases": [{"input": "[3,2,0,-4] with cycle", "expected": "True"}]
    }
]

TIME_CHALLENGES = [
    {
        "title": "Quick Quiz: Basic Operations",
        "time_limit": 60,
        "questions": [0, 1, 2, 3, 4],  # Easy questions
        "bonus_points": 20
    },
    {
        "title": "Speed Round: Complexity Analysis",
        "time_limit": 90,
        "questions": [5, 6, 7, 8, 9],  # Medium questions
        "bonus_points": 30
    }
]

# Continue with the existing fallback quiz data
if 'QUIZ_QUESTIONS' not in locals():
    QUIZ_QUESTIONS = [
        {
            "question": "What is the time complexity of inserting an element at the beginning of a singly linked list?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
            "correct": 0,
            "explanation": "Inserting at the beginning requires only updating the head pointer, which is O(1) time.",
            "difficulty": "easy",
            "points": 10
        },
        {
            "question": "In a doubly linked list, each node contains:",
            "options": ["Only data", "Data and one pointer", "Data and two pointers", "Data and three pointers"],
            "correct": 2,
            "explanation": "Doubly linked list nodes contain data, a previous pointer, and a next pointer.",
            "difficulty": "easy",
            "points": 10
        },
        {
            "question": "Which linked list type has the last node pointing back to the first node?",
            "options": ["Singly linked list", "Doubly linked list", "Circular linked list", "XOR linked list"],
            "correct": 2,
            "explanation": "Circular linked lists form a loop by pointing the last node to the first.",
            "difficulty": "easy",
            "points": 10
        },
        {
            "question": "What does NULL represent in a linked list?",
            "options": ["Empty data", "End of list", "Beginning of list", "Invalid node"],
            "correct": 1,
            "explanation": "NULL indicates the end of the linked list where no more nodes exist.",
            "difficulty": "easy",
            "points": 10
        },
        {
            "question": "Which operation is typically O(1) in a linked list?",
            "options": ["Insertion at beginning", "Searching", "Traversal", "Deletion by value"],
            "correct": 0,
            "explanation": "Insertion at the beginning is constant time as it only requires updating the head pointer.",
            "difficulty": "easy",
            "points": 10
        },
        # Medium Questions
        {
            "question": "Which of the following is NOT an advantage of linked lists over arrays?",
            "options": ["Dynamic size", "Efficient random access", "No memory waste", "Flexible structure"],
            "correct": 1,
            "explanation": "Linked lists have poor random access (O(n)) compared to arrays (O(1)).",
            "difficulty": "medium",
            "points": 15
        },
        {
            "question": "What is the space complexity of a singly linked list with n elements?",
            "options": ["O(1)", "O(n)", "O(n²)", "O(log n)"],
            "correct": 1,
            "explanation": "Each node requires O(1) space, so n nodes require O(n) space.",
            "difficulty": "medium",
            "points": 15
        },
        {
            "question": "What is the time complexity of searching for an element in a linked list?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
            "correct": 1,
            "explanation": "Searching requires traversing the list, which is O(n) in the worst case.",
            "difficulty": "medium",
            "points": 15
        },
        {
            "question": "What is the main advantage of a doubly linked list over a singly linked list?",
            "options": ["Less memory usage", "Bidirectional traversal", "Simpler implementation", "Faster insertion at end"],
            "correct": 1,
            "explanation": "Doubly linked lists allow traversal in both forward and backward directions.",
            "difficulty": "medium",
            "points": 15
        },
        {
            "question": "In which scenario would you prefer a linked list over an array?",
            "options": ["Random access needed", "Frequent insertions/deletions", "Memory is limited", "Cache performance critical"],
            "correct": 1,
            "explanation": "Linked lists excel at frequent insertions and deletions, especially at the beginning.",
            "difficulty": "medium",
            "points": 15
        },
        {
            "question": "Which algorithm is commonly used to detect cycles in a linked list?",
            "options": ["Quick Sort", "Merge Sort", "Floyd's Cycle Detection", "Binary Search"],
            "correct": 2,
            "explanation": "Floyd's Cycle Detection algorithm uses two pointers moving at different speeds.",
            "difficulty": "hard",
            "points": 25
        },
        {
            "question": "What is a common use case for circular linked lists?",
            "options": ["Undo functionality", "Round-robin scheduling", "Browser history", "Polynomial representation"],
            "correct": 1,
            "explanation": "Circular linked lists are ideal for round-robin scheduling algorithms.",
            "difficulty": "hard",
            "points": 25
        }
    ]

try:
    from linked_list_classes import Node, SinglyLinkedList, DoublyLinkedList, CircularLinkedList
except ImportError:
    st.error("⚠️ linked_list_classes.py not found. Please ensure all files are in the same directory.")
    st.stop()

# Set page config
st.set_page_config(
    page_title="Linked List Data Structures",
    layout="wide",
    page_icon="🔗",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS for Modern UI/UX
st.markdown(r"""
<style>
    /* Import Modern Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    /* Root Variables for Design System */
    :root {
        /* Soft Modern Color Palette */
        --primary-50: #f0f9ff;
        --primary-100: #e0f2fe;
        --primary-200: #bae6fd;
        --primary-300: #7dd3fc;
        --primary-400: #38bdf8;
        --primary-500: #0ea5e9;
        --primary-600: #0284c7;
        --primary-700: #0369a1;
        --primary-800: #075985;
        --primary-900: #0c4a6e;
        
        --secondary-50: #fdf4ff;
        --secondary-100: #fae8ff;
        --secondary-200: #f5d0fe;
        --secondary-300: #f0abfc;
        --secondary-400: #e879f9;
        --secondary-500: #d946ef;
        --secondary-600: #c026d3;
        --secondary-700: #a21caf;
        --secondary-800: #86198f;
        --secondary-900: #701a75;
        
        --neutral-50: #fafafa;
        --neutral-100: #f5f5f5;
        --neutral-200: #e5e5e5;
        --neutral-300: #d4d4d4;
        --neutral-400: #a3a3a3;
        --neutral-500: #737373;
        --neutral-600: #525252;
        --neutral-700: #404040;
        --neutral-800: #262626;
        --neutral-900: #171717;
        
        --success-50: #f0fdf4;
        --success-100: #dcfce7;
        --success-200: #bbf7d0;
        --success-300: #86efac;
        --success-400: #4ade80;
        --success-500: #22c55e;
        --success-600: #16a34a;
        
        --warning-50: #fffbeb;
        --warning-100: #fef3c7;
        --warning-200: #fde68a;
        --warning-300: #fcd34d;
        --warning-400: #fbbf24;
        --warning-500: #f59e0b;
        --warning-600: #d97706;
        
        --error-50: #fef2f2;
        --error-100: #fee2e2;
        --error-200: #fecaca;
        --error-300: #fca5a5;
        --error-400: #f87171;
        --error-500: #ef4444;
        --error-600: #dc2626;
        
        /* Shadows */
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        
        /* Border Radius */
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
        --radius-2xl: 24px;
        --radius-full: 9999px;
        
        /* Transitions */
        --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-normal: 250ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Base Styles */
    .stApp {
        background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: var(--neutral-700);
        line-height: 1.6;
    }
    
    /* Dark Mode */
    @media (prefers-color-scheme: dark) {
        .stApp {
            background: linear-gradient(135deg, #0c0a09 0%, #171717 100%);
            color: var(--neutral-200);
        }
    }
    
    /* Remove default padding */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Space Grotesk', Inter, sans-serif;
        font-weight: 600;
        color: var(--neutral-800);
        letter-spacing: -0.025em;
        margin-bottom: 1rem;
    }
    
    h1 {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--primary-600) 0%, var(--secondary-600) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        font-size: 2.25rem;
        font-weight: 600;
    }
    
    h3 {
        font-size: 1.875rem;
        font-weight: 600;
    }
    
    p, li, span {
        color: var(--neutral-600);
        line-height: 1.7;
    }
    
    /* Dark mode text colors */
    @media (prefers-color-scheme: dark) {
        h1, h2, h3, h4, h5, h6 {
            color: var(--neutral-100);
        }
        
        p, li, span {
            color: var(--neutral-300);
        }
    }
    
    /* Glassmorphism Cards */
    .section-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        border-radius: var(--radius-xl);
        padding: 2.5rem;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-lg);
        transition: all var(--transition-normal);
    }
    
    .section-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-xl);
    }
    
    @media (prefers-color-scheme: dark) {
        .section-card {
            background: rgba(23, 23, 23, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--neutral-200);
        }
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.1) 0%, rgba(217, 70, 239, 0.1) 100%);
        border: 1px solid rgba(14, 165, 233, 0.2);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1rem;
        text-align: center;
        transition: all var(--transition-normal);
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-6px) scale(1.02);
        border-color: rgba(14, 165, 233, 0.4);
        box-shadow: var(--shadow-xl);
    }
    
    /* Modern Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-500) 0%, var(--secondary-500) 100%);
        color: white;
        border: none;
        border-radius: var(--radius-lg);
        padding: 0.875rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all var(--transition-normal);
        box-shadow: var(--shadow-md);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Form Inputs */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(14, 165, 233, 0.2);
        border-radius: var(--radius-lg);
        padding: 1rem 1.25rem;
        font-size: 1rem;
        transition: all var(--transition-fast);
        box-shadow: var(--shadow-sm);
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: var(--primary-400);
        box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1), var(--shadow-md);
        outline: none;
    }
    
    @media (prefers-color-scheme: dark) {
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            background: rgba(23, 23, 23, 0.8);
            border-color: rgba(14, 165, 233, 0.3);
            color: var(--neutral-200);
        }
    }
    
    /* Select Boxes */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(14, 165, 233, 0.2);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-sm);
        transition: all var(--transition-fast);
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--primary-400);
        box-shadow: var(--shadow-md);
    }
    
    @media (prefers-color-scheme: dark) {
        .stSelectbox > div > div {
            background: rgba(23, 23, 23, 0.8);
            border-color: rgba(14, 165, 233, 0.3);
        }
    }
    
    /* Status Messages */
    .stSuccess {
        background: linear-gradient(135deg, var(--success-400) 0%, var(--success-500) 100%);
        border-radius: var(--radius-lg);
        border: none;
        box-shadow: var(--shadow-md);
        color: white;
        font-weight: 500;
    }
    
    .stError {
        background: linear-gradient(135deg, var(--error-400) 0%, var(--error-500) 100%);
        border-radius: var(--radius-lg);
        border: none;
        box-shadow: var(--shadow-md);
        color: white;
        font-weight: 500;
    }
    
    .stWarning {
        background: linear-gradient(135deg, var(--warning-400) 0%, var(--warning-500) 100%);
        border-radius: var(--radius-lg);
        border: none;
        box-shadow: var(--shadow-md);
        color: white;
        font-weight: 500;
    }
    
    .stInfo {
        background: linear-gradient(135deg, var(--primary-400) 0%, var(--primary-500) 100%);
        border-radius: var(--radius-lg);
        border: none;
        box-shadow: var(--shadow-md);
        color: white;
        font-weight: 500;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    @media (prefers-color-scheme: dark) {
        .css-1d391kg {
            background: rgba(23, 23, 23, 0.9);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        h1 {
            font-size: 2.25rem;
        }
        
        h2 {
            font-size: 1.875rem;
        }
        
        .section-card {
            padding: 1.75rem;
            margin: 1.5rem 0;
        }
        
        .feature-card {
            padding: 1.5rem;
            margin: 0.75rem;
        }
        
        .stButton > button {
            padding: 0.75rem 1.5rem;
            font-size: 0.95rem;
        }
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .animate-fadeInUp {
        animation: fadeInUp 0.6s ease-out;
    }
    
    .animate-float {
        animation: float 3s ease-in-out infinite;
    }
    
    @media (prefers-color-scheme: dark) {
        .main-header {
            color: #f1f5f9;
        }
    }
    
    /* Cards */
    .section-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }
    
    @media (prefers-color-scheme: dark) {
        .section-card {
            background: #1e293b;
            border-color: #334155;
            color: #e2e8f0;
        }
    }
    
    .feature-card {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.75rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
    }
    
    /* Timeline */
    .timeline {
        position: relative;
        padding-left: 30px;
    }
    
    .timeline::before {
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 2px;
        background: #6366f1;
    }
    
    .timeline-item {
        position: relative;
        margin-bottom: 2rem;
        padding-left: 30px;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -22px;
        top: 8px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #6366f1;
    }
    
    .timeline-content {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #6366f1;
        color: #1e293b;
    }
    
    @media (prefers-color-scheme: dark) {
        .timeline-content {
            background: #334155;
            color: #e2e8f0;
        }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }
    
    /* Metrics */
    .metric-card {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.75rem;
    }
    
    /* Visual diagram */
    .visual-diagram {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
        color: #1e293b;
    }
    
    @media (prefers-color-scheme: dark) {
        .visual-diagram {
            background: #334155;
            border-color: #475569;
            color: #e2e8f0;
        }
    }
    
    /* Progress bar */
    .progress-container {
        background: #f1f5f9;
        border-radius: 25px;
        padding: 3px;
        margin: 1rem 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        height: 20px;
        border-radius: 22px;
        transition: width 1s ease-in-out;
    }
    
    @media (prefers-color-scheme: dark) {
        .progress-container {
            background: #475569;
        }
    }
    
    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #1e293b;
    }
    
    p, span, div {
        color: #475569;
    }
    
    @media (prefers-color-scheme: dark) {
        h1, h2, h3, h4, h5, h6 {
            color: #f1f5f9;
        }
        
        p, span, div {
            color: #cbd5e1;
        }
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .section-card {
            padding: 1rem;
            margin: 1rem 0;
        }
        
        .feature-card {
            padding: 1rem;
            margin: 0.5rem;
        }
        --error-color: #ef4444;
        --warning-color: #f97316;
        --info-color: #3b82f6;
        --success-color: #22c55e;
        
        /* Light Mode Colors */
        --bg-primary: #ffffff;
        --bg-secondary: #f8fafc;
        --bg-tertiary: #f1f5f9;
        --text-primary: #1e293b;
        --text-secondary: #64748b;
        --text-muted: #94a3b8;
        --border-color: #e2e8f0;
        --shadow-light: rgba(0, 0, 0, 0.05);
        --shadow-medium: rgba(0, 0, 0, 0.1);
        --shadow-heavy: rgba(0, 0, 0, 0.15);
    }
    
    /* Dark Mode Colors */
    [data-theme="dark"] {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-tertiary: #334155;
        --text-primary: #f1f5f9;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --border-color: #475569;
        --shadow-light: rgba(0, 0, 0, 0.2);
        --shadow-medium: rgba(0, 0, 0, 0.3);
        --shadow-heavy: rgba(0, 0, 0, 0.4);
    }
    
    /* Auto-detect system theme */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-tertiary: #334155;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --border-color: #475569;
            --shadow-light: rgba(0, 0, 0, 0.2);
            --shadow-medium: rgba(0, 0, 0, 0.3);
            --shadow-heavy: rgba(0, 0, 0, 0.4);
        }
    }
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: var(--bg-primary);
        color: var(--text-primary);
    }
    
    /* Main Header */
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out;
        letter-spacing: -0.02em;
    }
    
    .subtitle {
        font-size: 1.25rem;
        color: var(--text-secondary);
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    [data-theme="dark"] .main-header {
        background: linear-gradient(45deg, #64b5f6, #42a5f5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .section-card {
        background: var(--background-color, rgba(255, 255, 255, 0.95));
        border-radius: 15px;
        padding: 2.5rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        border-left: 6px solid #1e3c72;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    [data-theme="dark"] .section-card {
        background: rgba(30, 30, 30, 0.95);
        box-shadow: 0 8px 25px rgba(255, 255, 255, 0.05);
    }

    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }

    .section-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #1e3c72, #2a5298, #667eea);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .section-card:hover::before {
        opacity: 1;
    }

    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 0.75rem;
        text-align: center;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
    }

    .feature-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.3s ease;
        opacity: 0;
    }

    .feature-card:hover::after {
        opacity: 1;
        animation: shimmer 1.5s ease-in-out;
    }

    /* Interactive Elements */
    .interactive-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .interactive-card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(245, 87, 108, 0.3);
    }

    .code-block {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: #ecf0f1;
        border-left: 4px solid #1e3c72;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-radius: 10px;
        position: relative;
        font-family: 'Fira Code', 'Monaco', 'Consolas', monospace;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .code-block::before {
        content: '💻';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 1.2rem;
        opacity: 0.7;
    }

    .highlight-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border: 2px solid #2196f3;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        position: relative;
        animation: pulse 2s infinite;
        color: #1565c0;
    }
    
    [data-theme="dark"] .highlight-box {
        background: linear-gradient(135deg, rgba(33, 150, 243, 0.2) 0%, rgba(33, 150, 243, 0.1) 100%);
        border: 2px solid #42a5f5;
        color: #90caf9;
    }

    .highlight-box::before {
        content: '💡';
        position: absolute;
        top: -10px;
        left: 20px;
        background: var(--background-color, white);
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    [data-theme="dark"] .highlight-box::before {
        background: #2c2c2c;
        box-shadow: 0 2px 10px rgba(255, 255, 255, 0.1);
    }

    /* Progress and Metrics */
    .progress-container {
        background: #f8f9fa;
        border-radius: 25px;
        padding: 3px;
        margin: 1rem 0;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .progress-bar {
        background: linear-gradient(90deg, #1e3c72, #667eea);
        height: 20px;
        border-radius: 22px;
        transition: width 1s ease-in-out;
        position: relative;
        overflow: hidden;
    }

    .progress-bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shimmer 2s infinite;
    }

    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.75rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        position: relative;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
    }

    .metric-card .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .metric-card .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Tab Enhancements */
    .tab-content {
        padding: 2rem 0;
        animation: fadeIn 0.5s ease-out;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 10px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(30, 60, 114, 0.4);
        transform: translateY(-2px);
    }

    .stTabs [aria-selected="true"]::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }

    /* Quiz Section Styling */
    .quiz-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .quiz-question {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .quiz-options {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .quiz-options:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateX(5px);
    }
    
    .difficulty-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .difficulty-easy {
        background: #4CAF50;
        color: white;
    }
    
    .difficulty-medium {
        background: #FF9800;
        color: white;
    }
    
    .difficulty-hard {
        background: #F44336;
        color: white;
    }
    
    .quiz-progress {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        height: 8px;
        margin: 1rem 0;
        overflow: hidden;
    }
    
    .quiz-progress-fill {
        background: linear-gradient(90deg, #4CAF50, #8BC34A);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    .quiz-score {
        background: linear-gradient(135deg, #4CAF50 0%, #8BC34A 100%);
        color: white;
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.3);
    }
    
    .quiz-explanation {
        background: linear-gradient(135deg, #2196F3 0%, #21CBF3 100%);
        color: white;
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #0D47A1;
    }
    
    /* Gamification Elements */
    .achievement-badge {
        background: linear-gradient(135deg, #FFD700 0%, #FFA000 100%);
        color: #333;
        border-radius: 25px;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        display: inline-block;
        font-weight: bold;
        box-shadow: 0 3px 10px rgba(255, 215, 0, 0.3);
        animation: bounce 0.5s ease;
    }
    
    .leaderboard-entry {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(5px);
    }
    
    .time-challenge-timer {
        background: linear-gradient(135deg, #FF5722 0%, #FF9800 100%);
        color: white;
        border-radius: 50px;
        padding: 1rem 2rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(255, 87, 34, 0.3);
        animation: pulse 1s infinite;
    }
    
    /* Animation Keyframes */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }

    /* Interactive Buttons */
    .modern-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }

    .modern-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }

    .modern-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s ease;
    }

    .modern-button:hover::before {
        left: 100%;
    }

    /* Enhanced Code Blocks */
    .code-container {
        position: relative;
        margin: 1.5rem 0;
    }

    .code-header {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 8px 8px 0 0;
        font-size: 0.9rem;
        font-weight: 600;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .code-content {
        background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
        color: #ecf0f1;
        padding: 1.5rem;
        border-radius: 0 0 8px 8px;
        font-family: 'Fira Code', 'Monaco', 'Consolas', monospace;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        position: relative;
    }

    .copy-button {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 0.8rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .copy-button:hover {
        background: rgba(255,255,255,0.2);
        transform: scale(1.05);
    }

    /* Visual Enhancements */
    .visual-diagram {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        position: relative;
        color: #2c3e50;
    }
    
    [data-theme="dark"] .visual-diagram {
        background: linear-gradient(135deg, #2c2c2c 0%, #1e1e1e 100%);
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.05);
        color: #e0e0e0;
    }

    .visual-diagram::before {
        content: '🎨';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.5rem;
        opacity: 0.6;
    }
    
    /* Dark mode compatibility for text colors */
    [data-theme="dark"] h1, [data-theme="dark"] h2, [data-theme="dark"] h3, [data-theme="dark"] h4, [data-theme="dark"] h5 {
        color: #e0e0e0 !important;
    }
    
    [data-theme="dark"] p, [data-theme="dark"] li, [data-theme="dark"] span {
        color: #b0b0b0 !important;
    }
    
    [data-theme="dark"] strong {
        color: #ffffff !important;
    }

    /* Interactive Timeline */
    .timeline {
        position: relative;
        padding-left: 30px;
    }

    .timeline::before {
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, #1e3c72, #667eea);
    }

    .timeline-item {
        position: relative;
        margin-bottom: 2rem;
        padding-left: 30px;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -22px;
        top: 8px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1e3c72, #667eea);
        box-shadow: 0 0 0 3px rgba(30, 60, 114, 0.2);
    }

    .timeline-content {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #1e3c72;
    }

    /* Floating Action Elements */
    .floating-element {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        z-index: 1000;
    }

    .floating-element:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }

        .section-card {
            padding: 1.5rem;
            margin: 1rem 0;
        }

        .feature-card {
            padding: 1.5rem;
            margin: 0.5rem;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            font-size: 0.9rem;
        }
    }

    /* Loading Animation */
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255,255,255,0.3);
        border-radius: 50%;
        border-top-color: white;
        animation: spin 1s ease-in-out infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* Success Animation */
    .success-checkmark {
        display: inline-block;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #4CAF50;
        position: relative;
    }

    .success-checkmark::after {
        content: '✓';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-weight: bold;
        animation: checkmark 0.5s ease-in-out;
    }

    @keyframes checkmark {
        0% { transform: translate(-50%, -50%) scale(0); }
        50% { transform: translate(-50%, -50%) scale(1.2); }
        100% { transform: translate(-50%, -50%) scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'username' not in st.session_state:
    st.session_state.username = "Guest"
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'achievements' not in st.session_state:
    st.session_state.achievements = []
if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []
if 'notes' not in st.session_state:
    st.session_state.notes = {}
if 'progress' not in st.session_state:
    st.session_state.progress = {}
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []
if 'quiz_attempts' not in st.session_state:
    st.session_state.quiz_attempts = 0
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0
if 'coding_challenge_score' not in st.session_state:
    st.session_state.coding_challenge_score = 0
if 'time_challenge_best' not in st.session_state:
    st.session_state.time_challenge_best = {}

# Helper functions
def save_progress(section):
    st.session_state.progress[section] = True

def add_bookmark(section):
    if section not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(section)

def save_note(section, note):
    st.session_state.notes[section] = {
        'text': note,
        'timestamp': pd.Timestamp.now()
    }

def step_by_step_insert(elements, value, position):
    steps = [
        f"Step 1: Create new node with value {value}",
        f"Step 2: Set up pointers for insertion at position {position}",
        f"Step 3: Update existing node connections",
        f"Step 4: Insert complete! New list: {elements[:position] + [value] + elements[position:]}"
    ]
    return steps

def export_code(code, filename):
    st.download_button(
        label="📥 Download Code",
        data=code,
        file_name=filename,
        mime="text/plain"
    )

# Enhanced Welcome/Dashboard section with modern UI/UX
def welcome_dashboard():
    st.markdown('<h1 class="main-header" style="margin-top: 0; padding-top: 0;">🔗 Linked List Data Structures</h1>', unsafe_allow_html=True)
    save_progress("Welcome")

    st.markdown("""
    <div class="section-card" style="margin-top: 0.5rem; background: linear-gradient(135deg, var(--primary-50) 0%, var(--secondary-50) 100%); border: 1px solid rgba(14, 165, 233, 0.1); box-shadow: var(--shadow-lg);">
    <h2 style="color: var(--text-primary); text-align: center; margin-bottom: 1rem; font-weight: 700;">Welcome to Your Interactive Learning Journey!</h2>
    <p style="font-size: 1.2em; text-align: center; color: var(--text-secondary); margin-bottom: 1rem; font-weight: 400;">
    Master linked lists through interactive visualizations, hands-on practice, and comprehensive analysis.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add Start Learning button with modern styling
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Start Learning", key="start_learning", use_container_width=True, help="Begin your linked list learning journey"):
            st.session_state.current_tab = 1  # Navigate to Introduction
            st.session_state.scroll_to_top = True  # Flag to scroll to top
            st.rerun()

    # Interactive Feature cards with modern soft UI design
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.1s; background: linear-gradient(135deg, var(--primary-400) 0%, var(--primary-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-lg); transition: all var(--transition-normal); cursor: pointer; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
        <h3 style="margin: 0 0 0.5rem 0; font-weight: 700;">Learn</h3>
        <p style="margin: 0 0 1rem 0; opacity: 0.9; font-weight: 400;">Comprehensive guide to singly, doubly, and circular linked lists</p>
        <div style="background: rgba(255,255,255,0.2); border-radius: var(--radius-full); padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 500;">
            Interactive Examples
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.2s; background: linear-gradient(135deg, var(--secondary-400) 0%, var(--secondary-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-lg); transition: all var(--transition-normal); cursor: pointer; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🎮</div>
        <h3 style="margin: 0 0 0.5rem 0; font-weight: 700;">Practice</h3>
        <p style="margin: 0 0 1rem 0; opacity: 0.9; font-weight: 400;">Interactive playground with real-time operations</p>
        <div style="background: rgba(255,255,255,0.2); border-radius: var(--radius-full); padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 500;">
            Live Visualization
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.3s; background: linear-gradient(135deg, var(--accent-400) 0%, var(--accent-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-lg); transition: all var(--transition-normal); cursor: pointer; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
        <h3 style="margin: 0 0 0.5rem 0; font-weight: 700;">Analyze</h3>
        <p style="margin: 0 0 1rem 0; opacity: 0.9; font-weight: 400;">Performance comparisons and optimization tips</p>
        <div style="background: rgba(255,255,255,0.2); border-radius: var(--radius-full); padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 500;">
            Big O Analysis
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.4s; background: linear-gradient(135deg, var(--success-400) 0%, var(--success-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-lg); transition: all var(--transition-normal); cursor: pointer; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 3rem; margin-bottom: 1rem;">💡</div>
        <h3 style="margin: 0 0 0.5rem 0; font-weight: 700;">Solve</h3>
        <p style="margin: 0 0 1rem 0; opacity: 0.9; font-weight: 400;">Practice problems with detailed solutions</p>
        <div style="background: rgba(255,255,255,0.2); border-radius: var(--radius-full); padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 500;">
            Step-by-Step Solutions
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced Quick stats with modern metric cards
    st.markdown('<div class="section-card" style="margin-top: 1rem; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border: 1px solid rgba(14, 165, 233, 0.1); box-shadow: var(--shadow-lg);">', unsafe_allow_html=True)
    st.subheader("🚀 Quick Start Guide")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, var(--primary-400) 0%, var(--primary-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-md); transition: all var(--transition-normal); border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">3</div>
        <div style="font-weight: 600; margin-bottom: 0.5rem; font-size: 1.1rem;">Data Structures</div>
        <div style="font-size: 0.875rem; opacity: 0.9;">Singly, Doubly, Circular</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, var(--secondary-400) 0%, var(--secondary-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-md); transition: all var(--transition-normal); border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">8+</div>
        <div style="font-weight: 600; margin-bottom: 0.5rem; font-size: 1.1rem;">Operations</div>
        <div style="font-size: 0.875rem; opacity: 0.9;">Insert, Delete, Search, Traverse</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, var(--accent-400) 0%, var(--accent-500) 100%); color: white; border-radius: var(--radius-xl); padding: 2rem; text-align: center; box-shadow: var(--shadow-md); transition: all var(--transition-normal); border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem;">10+</div>
        <div style="font-weight: 600; margin-bottom: 0.5rem; font-size: 1.1rem;">Practice Problems</div>
        <div style="font-size: 0.875rem; opacity: 0.9;">With Detailed Solutions</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    /* Sidebar Enhancements */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--bg-secondary) 0%, var(--bg-tertiary) 100%);
        border-right: 1px solid var(--border-color);
    }
    
    /* Streamlit component styling */
    .stSelectbox > div > div {
        background: var(--bg-secondary);
        border: 2px solid var(--border-color);
        border-radius: 12px;
        color: var(--text-primary);
    }
    
    .stTextInput > div > div > input {
        background: var(--bg-secondary);
        border: 2px solid var(--border-color);
        border-radius: 12px;
        color: var(--text-primary);
        padding: 12px 16px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-hover) 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
    }
    
    /* Message styling */
    .stSuccess {
        background: linear-gradient(135deg, var(--success-color) 0%, #16a085 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(34, 197, 94, 0.3);
    }
    
    .stError {
        background: linear-gradient(135deg, var(--danger-color) 0%, #c0392b 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
    }
    
    .stWarning {
        background: linear-gradient(135deg, var(--warning-color) 0%, #d68910 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(249, 115, 22, 0.3);
    }
    
    .stInfo {
        background: linear-gradient(135deg, var(--info-color) 0%, #2980b9 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    /* Dark mode text visibility */
    @media (prefers-color-scheme: dark) {
        .stMarkdown, .stText, p, span, div {
            color: var(--text-primary) !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary) !important;
        }
    }
    
    /* Remove top padding/margin */
    .main .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    
    .main-header {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .section-card {
            padding: 1rem;
            margin: 0.5rem 0;
        }
        
        .feature-card {
            padding: 1rem;
            margin: 0.25rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Enhanced Progress indicator with visual progress bar
    st.markdown('<div class="section-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.subheader("📈 Learning Progress")

    # Progress visualization
    st.markdown("""
    <div style="margin: 2rem 0;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
    <span style="font-weight: 600; color: #1e3c72;">Your Progress</span>
    <span style="font-weight: 600; color: #1e3c72;">0%</span>
    </div>
    <div class="progress-container">
    <div class="progress-bar" style="width: 0%;"></div>
    </div>
    <div style="margin-top: 1rem; font-size: 0.9em; color: #666;">
    Complete sections to track your progress and unlock achievements! 🏆
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive learning path
    st.markdown("""
    <div class="visual-diagram">
    <h4 style="margin-bottom: 1.5rem; color: #1e3c72;">🎯 Learning Path</h4>
    <div class="timeline">
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>📖 Introduction</h5>
    <p>Learn the fundamentals of linked lists</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>🔗 Types</h5>
    <p>Explore singly, doubly, and circular variants</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>⚙️ Operations</h5>
    <p>Master insertion, deletion, and traversal</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>🎮 Playground</h5>
    <p>Practice with interactive visualizations</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>📊 Analysis</h5>
    <p>Understand performance characteristics</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>💡 Practice</h5>
    <p>Solve challenging problems</p>
    </div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Main navigation
def main():
    st.markdown('<style>.main .block-container { padding-top: 0 !important; }</style>', unsafe_allow_html=True)
    
    # Sidebar navigation with modern soft UI styling
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 2rem 1rem; margin-bottom: 2rem; background: linear-gradient(135deg, var(--primary-400) 0%, var(--secondary-400) 100%); border-radius: var(--radius-xl); box-shadow: var(--shadow-lg);">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔗</div>
        <h2 style="color: white; margin: 0; font-weight: 700; font-size: 1.25rem;">Linked Lists</h2>
        <p style="color: rgba(255,255,255,0.9); font-size: 0.875rem; margin: 0.5rem 0; font-weight: 400;">Interactive Learning Hub</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation menu with modern soft UI styling
    menu_options = [
        "🏠 Welcome",
        "📖 Introduction", 
        "🔗 Types of Lists",
        "⚙️ Operations",
        "🎮 Interactive Playground",
        "📊 Performance Analysis",
        "💡 Practice Problems",
        "🎯 Gamified Quiz",
        "🎨 Advanced Visualizations",
        "📝 Interview Prep",
        "📚 References"
    ]
    
    # Custom styled selectbox container
    st.sidebar.markdown("""
    <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border-radius: var(--radius-lg); padding: 1rem; margin-bottom: 2rem; border: 1px solid rgba(14, 165, 233, 0.1);">
        <label style="color: var(--text-primary); font-weight: 600; margin-bottom: 0.5rem; display: block;">Navigation Menu</label>
    </div>
    """, unsafe_allow_html=True)
    
    selected = st.sidebar.selectbox(
        "",
        menu_options,
        key="main_nav",
        help="Select a learning section to explore"
    )
    
    # User profile in sidebar with modern soft UI cards
    with st.sidebar.expander("👤 Profile", expanded=False):
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, var(--primary-400) 0%, var(--primary-500) 100%); color: white; padding: 1.5rem; border-radius: var(--radius-lg); margin-bottom: 1rem; box-shadow: var(--shadow-md);">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">👤</div>
            <div style="font-weight: 600; margin-bottom: 0.25rem;">{st.session_state.username}</div>
            <div style="font-size: 0.875rem; opacity: 0.9;">Learner</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats in a modern card
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border-radius: var(--radius-lg); padding: 1rem; border: 1px solid rgba(14, 165, 233, 0.1); margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="color: var(--text-secondary);">Score</span>
                <span style="font-weight: 700; color: var(--primary-500);">{st.session_state.user_score}</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: var(--text-secondary);">Achievements</span>
                <span style="font-weight: 700; color: var(--success-500);">{len(st.session_state.achievements)}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.achievements:
            st.markdown("""
            <div style="background: linear-gradient(135deg, var(--success-400) 0%, var(--success-500) 100%); color: white; padding: 1rem; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);">
                <div style="font-weight: 600; margin-bottom: 0.5rem;">🎉 Latest Achievement</div>
                <div style="font-size: 0.875rem;">""" + st.session_state.achievements[-1] + """</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Progress tracker with modern design
    with st.sidebar.expander("📈 Progress", expanded=False):
        total_sections = len(menu_options) - 1  # Exclude welcome
        completed = len(st.session_state.progress)
        progress_pct = (completed / total_sections) * 100 if total_sections > 0 else 0
        
        # Modern progress card
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border-radius: var(--radius-lg); padding: 1.5rem; border: 1px solid rgba(14, 165, 233, 0.1); margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <span style="color: var(--text-secondary); font-weight: 500;">Overall Progress</span>
                <span style="font-weight: 700; color: var(--primary-500);">{progress_pct:.1f}%</span>
            </div>
            <div style="background: var(--neutral-200); border-radius: var(--radius-full); height: 8px; margin-bottom: 1rem;">
                <div style="background: linear-gradient(90deg, var(--primary-400), var(--secondary-400)); border-radius: var(--radius-full); height: 100%; width: {progress_pct}%; transition: width 0.5s ease;"></div>
            </div>
            <div style="text-align: center; color: var(--text-secondary); font-size: 0.875rem;">
                {completed} of {total_sections} sections completed
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Bookmarks with modern design
    if st.session_state.bookmarks:
        with st.sidebar.expander("📌 Bookmarks", expanded=False):
            st.markdown("""
            <div style="background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border-radius: var(--radius-lg); padding: 1rem; border: 1px solid rgba(14, 165, 233, 0.1);">
            """, unsafe_allow_html=True)
            for bookmark in st.session_state.bookmarks:
                st.markdown(f"""
                <div style="display: flex; align-items: center; padding: 0.5rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.5); border-radius: var(--radius-md); border-left: 3px solid var(--primary-400);">
                    <span style="margin-right: 0.5rem;">📌</span>
                    <span style="font-weight: 500; color: var(--text-primary);">{bookmark}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Route to appropriate section
    if selected == "🏠 Welcome":
        welcome_dashboard()
    elif selected == "📖 Introduction":
        introduction()
    elif selected == "🔗 Types of Lists":
        types_of_linked_lists()
    elif selected == "⚙️ Operations":
        operations_and_algorithms()
    elif selected == "🎮 Interactive Playground":
        interactive_playground()
    elif selected == "📊 Performance Analysis":
        performance_analysis()
    elif selected == "💡 Practice Problems":
        practice_problems()
    elif selected == "🎯 Gamified Quiz":
        interactive_quiz()
    elif selected == "🎨 Advanced Visualizations":
        advanced_visualizations()
    elif selected == "📝 Interview Prep":
        interview_preparation()
    elif selected == "📚 References":
        references_and_resources()

# Enhanced Introduction section with modern UI/UX
def introduction():
    st.markdown('<h1 class="main-header" style="margin-top: 0;">📖 Introduction to Linked Lists</h1>', unsafe_allow_html=True)
    save_progress("Introduction")
    
    # Section tools
    col1, col2 = st.columns([1, 1])
    with col1:
        is_bookmarked = "Introduction" in st.session_state.bookmarks
        if st.button("📌 Unbookmark" if is_bookmarked else "📌 Bookmark", key="bookmark_intro"):
            if is_bookmarked:
                st.session_state.bookmarks.remove("Introduction")
            else:
                add_bookmark("Introduction")
            st.rerun()
    with col2:
        if st.button("📝 Add Note", key="note_intro"):
            st.session_state.show_note_intro = True
    
    if st.session_state.get('show_note_intro', False):
        note_text = st.text_input("Your note:", key="intro_note_input")
        if st.button("Save", key="save_intro_note"):
            if note_text:
                save_note("Introduction", note_text)
                st.session_state.show_note_intro = False
                st.rerun()
    
    # Show existing note
    if "Introduction" in st.session_state.notes:
        with st.expander("📝 Your Note"):
            st.write(st.session_state.notes["Introduction"]['text'])

    # Interactive concept overview
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #1e3c72; text-align: center; margin-bottom: 1.5rem;">What is a Linked List?</h2>
    <div style="text-align: center; margin-bottom: 2rem;">
    <div class="highlight-box">
    <strong>A linked list is a fundamental data structure that consists of a sequence of elements called nodes.</strong>
    <br><br>
    Each node contains two parts:
    <ul style="text-align: left; display: inline-block; margin-top: 1rem;">
    <li><strong>Data</strong>: The actual information stored in the node</li>
    <li><strong>Reference/Pointer</strong>: A link to the next node in the sequence</li>
    </ul>
    </div>
    </div>
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
    <strong>Key Difference from Arrays:</strong> Unlike arrays, linked lists do not store elements in contiguous memory locations.
    Instead, each node points to the next one, forming a chain-like structure that provides dynamic memory allocation.
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Advantages/Disadvantages with interactive cards
    st.header("Why Use Linked Lists?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="interactive-card" style="border-left: 4px solid #4CAF50;">
        <h3 style="color: #4CAF50; margin-bottom: 1rem;">✅ Advantages</h3>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">🔸</span>
        <strong>Dynamic Size:</strong> Can grow or shrink during runtime
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">⚡</span>
        <strong>Efficient Operations:</strong> O(1) for insertions/deletions at known positions
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">💾</span>
        <strong>No Memory Waste:</strong> Only allocates memory when needed
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">🔧</span>
        <strong>Flexible Structure:</strong> Easy to implement stacks, queues, and other data structures
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="interactive-card" style="border-left: 4px solid #f44336;">
        <h3 style="color: #f44336; margin-bottom: 1rem;">❌ Disadvantages</h3>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">🎯</span>
        <strong>Random Access:</strong> O(n) time to access elements by index
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">📊</span>
        <strong>Extra Memory:</strong> Each node requires additional space for pointers
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">➡️</span>
        <strong>Sequential Access:</strong> Must traverse from beginning for most operations
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">⚡</span>
        <strong>Cache Performance:</strong> Poor locality of reference
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced Node Structure with interactive code block
    st.header("Basic Node Structure")

    st.markdown("""
    <div class="code-container">
    <div class="code-header">
    <span>🔧 Node Implementation</span>
    <button class="copy-button" onclick="navigator.clipboard.writeText(`class Node:\\n    def __init__(self, data):\\n        self.data = data\\n        self.next = None`)">Copy</button>
    </div>
    <div class="code-content">
class Node:
    def __init__(self, data):
        self.data = data        # The actual data stored in the node
        self.next = None        # Pointer to the next node (None if last node)
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Real-World Applications
    st.header("Real-World Applications")

    applications = [
        {"icon": "🎵", "title": "Music Playlists", "desc": "Songs linked in sequence for easy navigation"},
        {"icon": "🌐", "title": "Browser History", "desc": "Web pages linked for back/forward navigation"},
        {"icon": "↩️", "title": "Undo Functionality", "desc": "Operations stored as linked list in editors"},
        {"icon": "🔗", "title": "Hash Tables", "desc": "Collision resolution using separate chaining"},
        {"icon": "💾", "title": "Memory Management", "desc": "Free memory blocks tracking in OS"},
        {"icon": "📈", "title": "Polynomial Representation", "desc": "Mathematical terms linked by degree"}
    ]

    cols = st.columns(3)
    for i, app in enumerate(applications):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="feature-card" style="animation-delay: {i * 0.1}s; min-height: 120px;">
            <h4 style="margin-bottom: 0.5rem;">{app['icon']} {app['title']}</h4>
            <p style="font-size: 0.9em; opacity: 0.9;">{app['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Enhanced Memory Representation with visual diagram
    st.header("Memory Representation")

    st.markdown("""
    <div class="visual-diagram">
    <h3 style="margin-bottom: 1rem; color: #1e3c72;">🔍 How Linked Lists are Stored in Memory</h3>
    <p style="margin-bottom: 1.5rem;">Visual representation of how linked list nodes are scattered in memory:</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced memory layout visualization
    st.markdown("""
    <div class="section-card">
    <div style="font-family: 'Courier New', monospace; background: #2c3e50; color: #ecf0f1; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
    <div style="text-align: center; margin-bottom: 1rem; color: #3498db; font-weight: bold;">Memory Layout Visualization</div>
    <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 1rem;">
    <div style="border: 2px solid #e74c3c; border-radius: 8px; padding: 1rem; background: #34495e; min-width: 150px;">
    <div style="text-align: center; color: #e74c3c; font-weight: bold; margin-bottom: 0.5rem;">Node 1</div>
    <div><strong>Data:</strong> 10</div>
    <div><strong>Next:</strong> 0x200 →</div>
    <div style="text-align: center; margin-top: 0.5rem; color: #95a5a6; font-size: 0.8em;">Address: 0x100</div>
    </div>
    <div style="color: #e74c3c; font-size: 1.5rem;">→</div>
    <div style="border: 2px solid #27ae60; border-radius: 8px; padding: 1rem; background: #34495e; min-width: 150px;">
    <div style="text-align: center; color: #27ae60; font-weight: bold; margin-bottom: 0.5rem;">Node 2</div>
    <div><strong>Data:</strong> 20</div>
    <div><strong>Next:</strong> 0x300 →</div>
    <div style="text-align: center; margin-top: 0.5rem; color: #95a5a6; font-size: 0.8em;">Address: 0x200</div>
    </div>
    <div style="color: #27ae60; font-size: 1.5rem;">→</div>
    <div style="border: 2px solid #f39c12; border-radius: 8px; padding: 1rem; background: #34495e; min-width: 150px;">
    <div style="text-align: center; color: #f39c12; font-weight: bold; margin-bottom: 0.5rem;">Node 3</div>
    <div><strong>Data:</strong> 30</div>
    <div><strong>Next:</strong> NULL</div>
    <div style="text-align: center; margin-top: 0.5rem; color: #95a5a6; font-size: 0.8em;">Address: 0x300</div>
    </div>
    </div>
    <div style="margin-top: 1rem; text-align: center; color: #95a5a6; font-style: italic;">
    Nodes are scattered in memory, connected only by pointers
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive learning checkpoint
    st.markdown("""
    <div class="section-card">
    <h3 style="color: #1e3c72; text-align: center; margin-bottom: 1rem;">🎯 Learning Checkpoint</h3>
    <div style="display: flex; justify-content: space-around; margin: 1.5rem 0;">
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #4CAF50;">✓</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Node Structure</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #4CAF50;">✓</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Memory Layout</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #2196F3;">○</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Types of Lists</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #9E9E9E;">○</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Operations</div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add Continue to Types button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Continue to Types →", key="continue_to_types", use_container_width=True):
            st.session_state.current_tab = 2  # Navigate to Types
            st.session_state.scroll_to_top = True  # Flag to scroll to top
            st.rerun()
    
    st.markdown("""
    <div class="section-card">
    </div>
    """, unsafe_allow_html=True)

# Types of Linked Lists section
def types_of_linked_lists():
    st.title("Types of Linked Lists")
    save_progress("Types")

    st.markdown("""
    Linked lists come in various forms, each with its own strengths and use cases. Understanding the differences
    between these types is crucial for choosing the right data structure for your specific needs.
    """)

    st.header("1. Singly Linked List")
    st.markdown("**Overview:** The most basic form of linked list where each node points only to the next node.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Node Structure:**
        ```python
        class Node:
            def __init__(self, data):
                self.data = data      # The actual data
                self.next = None      # Pointer to next node
        ```

        **Detailed Characteristics:**
        - **Memory Usage:** Minimal (1 pointer + data per node)
        - **Traversal:** Only forward direction
        - **Operations:** Simple to implement
        - **Performance:** O(1) for beginning operations, O(n) for end operations
        - **Memory Efficiency:** Good for large datasets with sequential access

        **Advantages:**
        - ✅ Simple implementation and understanding
        - ✅ Low memory overhead per node
        - ✅ Efficient for stack operations (LIFO)
        - ✅ Good cache performance for sequential access
        - ✅ Easy to implement recursive algorithms

        **Disadvantages:**
        - ❌ No backward traversal
        - ❌ O(n) time for random access
        - ❌ Cannot efficiently delete previous node
        - ❌ More complex reverse operations

        **Real-World Use Cases:**
        - **Stack Implementation:** Perfect for undo/redo functionality
        - **Queue Implementation:** Basic FIFO operations
        - **Hash Table Chaining:** Collision resolution in hash tables
        - **Memory Management:** Free memory block tracking
        - **Symbol Tables:** In compilers and interpreters
        - **Polynomial Operations:** Representing mathematical polynomials
        """)

        st.subheader("Visual Representation")
        st.code("""
Singly Linked List Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | --> | Next: 0x300       | --> | Next: None        |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300

Traversal: 10 -> 20 -> 30 -> NULL
        """)

    with col2:
        st.code("""
# Complete Singly Linked List Implementation
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete_from_beginning(self):
        if self.head is None:
            return None
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data

    def search(self, target):
        current = self.head
        position = 0
        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example Usage:
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
print(sll.traverse())  # [1, 2, 3]
        """, language="python")

    st.header("2. Doubly Linked List")
    st.markdown("**Overview:** Each node has pointers to both previous and next nodes, enabling bidirectional traversal.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Node Structure:**
        ```python
        class DoublyNode:
            def __init__(self, data):
                self.data = data      # The actual data
                self.next = None      # Pointer to next node
                self.prev = None      # Pointer to previous node
        ```

        **Detailed Characteristics:**
        - **Memory Usage:** Higher (2 pointers + data per node)
        - **Traversal:** Both forward and backward directions
        - **Operations:** More complex but more flexible
        - **Performance:** O(1) for beginning and end operations (with tail pointer)
        - **Memory Efficiency:** Less efficient than singly linked lists

        **Advantages:**
        - ✅ Bidirectional traversal
        - ✅ Efficient deletion of any node (if reference is known)
        - ✅ Can implement deque operations efficiently
        - ✅ Easier to implement complex data structures
        - ✅ Better for frequent insertions/deletions at both ends

        **Disadvantages:**
        - ❌ Higher memory overhead
        - ❌ More complex implementation
        - ❌ Extra pointer updates required
        - ❌ Slightly slower operations due to extra bookkeeping

        **Real-World Use Cases:**
        - **Browser History:** Back and forward navigation
        - **Text Editors:** Cursor movement and editing
        - **LRU Cache:** Most Recently Used page replacement
        - **Undo/Redo Stacks:** Bidirectional operation history
        - **Music Player:** Previous/next track navigation
        - **File System Navigation:** Directory traversal
        """)

        st.subheader("Visual Representation")
        st.code("""
Doubly Linked List Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Prev: None        |     | Prev: 0x100       |     | Prev: 0x200       |
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | <-- | Next: 0x300       | <-- | Next: None        |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300

Traversal: NULL <- 10 <-> 20 <-> 30 -> NULL
        """)

    with col2:
        st.code("""
# Complete Doubly Linked List Implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Tail pointer for O(1) end operations
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_from_beginning(self):
        if self.head is None:
            return None
        deleted_data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return deleted_data

    def traverse_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def traverse_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

# Example Usage:
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
print(dll.traverse_forward())   # [1, 2, 3]
print(dll.traverse_backward())  # [3, 2, 1]
        """, language="python")

    st.header("3. Circular Linked List")
    st.markdown("**Overview:** The last node points back to the first node, forming a circle.")
    
    # Sum calculation examples for understanding
    st.subheader("📊 Sum Calculation Examples")
    
    st.markdown("""
    **Understanding through Sum Operations:**
    Let's see how to calculate the sum of all elements in different linked list types.
    """)
    
    tab1, tab2, tab3 = st.tabs(["Singly Linked", "Doubly Linked", "Circular Linked"])
    
    with tab1:
        st.markdown("**Sum in Singly Linked List:**")
        st.code("""
# Calculate sum of all elements
def calculate_sum_singly(head):
    total = 0
    current = head
    
    while current:
        total += current.data
        current = current.next
    
    return total

# Example: [10, 20, 30] → Sum = 60
ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20) 
ll.insert_at_end(30)
print(f"Sum: {calculate_sum_singly(ll.head)}")  # Output: 60
        """, language="python")
    
    with tab2:
        st.markdown("**Sum in Doubly Linked List:**")
        st.code("""
# Calculate sum - can traverse forward or backward
def calculate_sum_doubly_forward(head):
    total = 0
    current = head
    
    while current:
        total += current.data
        current = current.next
    
    return total

def calculate_sum_doubly_backward(tail):
    total = 0
    current = tail
    
    while current:
        total += current.data
        current = current.prev
    
    return total

# Example: [10, 20, 30] → Sum = 60 (both directions)
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
print(f"Forward Sum: {calculate_sum_doubly_forward(dll.head)}")   # 60
print(f"Backward Sum: {calculate_sum_doubly_backward(dll.tail)}")  # 60
        """, language="python")
    
    with tab3:
        st.markdown("**Sum in Circular Linked List:**")
        st.code("""
# Calculate sum - must avoid infinite loop!
def calculate_sum_circular(head):
    if not head:
        return 0
    
    total = head.data
    current = head.next
    
    # Stop when we reach the starting node again
    while current != head:
        total += current.data
        current = current.next
    
    return total

# Alternative with counter for safety
def calculate_sum_circular_safe(head, size):
    total = 0
    current = head
    count = 0
    
    while current and count < size:
        total += current.data
        current = current.next
        count += 1
    
    return total

# Example: [10, 20, 30] → Sum = 60
cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
print(f"Sum: {calculate_sum_circular(cll.head)}")  # Output: 60
        """, language="python")
    
    # Interactive sum calculator
    st.subheader("🧮 Interactive Sum Calculator")
    
    calc_type = st.selectbox("Choose list type for sum calculation:", 
                            ["Singly Linked", "Doubly Linked", "Circular Linked"])
    
    calc_input = st.text_input("Enter numbers (comma-separated):", "10, 20, 30, 40")
    
    if st.button("Calculate Sum"):
        try:
            numbers = [int(x.strip()) for x in calc_input.split(",") if x.strip()]
            if numbers:
                total = sum(numbers)
                st.success(f"📊 **{calc_type} Sum Result:**")
                st.write(f"Numbers: {numbers}")
                st.write(f"Sum: {total}")
                st.write(f"Average: {total/len(numbers):.2f}")
                st.write(f"Count: {len(numbers)}")
                
                # Show step-by-step calculation
  with st.expander("Step-by-step calculation"):
    # show each number and the running total
    running_total = 0
    for idx, n in enumerate(numbers, start=1):
        running_total += n
        st.write(f"{idx}. {n} → running total: {running_total}")
    st.markdown("**Finished step-by-step calculation.**")

