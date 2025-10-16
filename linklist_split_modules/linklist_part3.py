# Auto-generated module (part 3)
    
    # Display top performers
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--text-primary); margin: 0 0 1rem 0; text-align: center;">🥇 Top Performers</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    rank_colors = ["#FFD700", "#C0C0C0", "#CD7F32", "#4CAF50", "#2196F3", "#9C27B0", "#FF9800", "#795548", "#607D8B", "#F44336"]
    rank_emoji = ["🥇", "🥈", "🥉"] + ["🏅"] * 7
    
    for i, entry in enumerate(sorted_leaderboard[:10]):
        medal_color = rank_colors[i] if i < len(rank_colors) else "#666"
        
        leaderboard_html = f"""
        <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; margin: 0.5rem 0; border: 1px solid rgba(255, 255, 255, 0.1); transition: all 0.3s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: {medal_color}; font-size: 1.2rem;">{rank_emoji[i]}</span>
                    <strong style="color: var(--text-primary);">#{i+1} {entry['username']}</strong>
                </div>
                <div style="display: flex; gap: 1rem; align-items: center;">
                    <span style="color: var(--success-green); font-weight: bold;">{entry['score']} pts</span>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">{entry['time']:.1f}s</span>
                </div>
            </div>
        </div>
        """
        st.markdown(leaderboard_html, unsafe_allow_html=True)
    
    # Personal stats
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--text-primary); margin: 0 0 1rem 0; text-align: center;">📊 Your Statistics</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    user_entries = [entry for entry in st.session_state.leaderboard 
                   if entry['username'] == st.session_state.username]
    
    if user_entries:
        best_score = max(entry['score'] for entry in user_entries)
        best_time = min(entry['time'] for entry in user_entries)
        total_attempts = len(user_entries)
        
        stats_html = f'''
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1rem 0;">
            <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
                <div style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.5rem;">Best Score</div>
                <div style="color: var(--primary-blue); font-size: 1.5rem; font-weight: bold;">{best_score}</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
                <div style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.5rem;">Best Time</div>
                <div style="color: var(--success-green); font-size: 1.5rem; font-weight: bold;">{best_time:.1f}s</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
                <div style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.5rem;">Total Attempts</div>
                <div style="color: var(--primary-purple); font-size: 1.5rem; font-weight: bold;">{total_attempts}</div>
            </div>
        </div>
        '''
        st.markdown(stats_html, unsafe_allow_html=True)
    
    # Achievements display
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--text-primary); margin: 0 0 1rem 0; text-align: center;">🏅 Your Achievements</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    if st.session_state.achievements:
        achievements_html = '<div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0;">'
        for achievement in st.session_state.achievements:
            achievements_html += f'''
            <span style="background: linear-gradient(135deg, var(--primary-gold) 0%, var(--primary-orange) 100%); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; font-weight: bold; box-shadow: 0 2px 8px rgba(255, 152, 0, 0.3);">{achievement}</span>
            '''
        achievements_html += '</div>'
        st.markdown(achievements_html, unsafe_allow_html=True)
    else:
        no_achievements_html = '''
        <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
            <p style="color: var(--text-secondary); margin: 0;">Complete challenges to earn achievements!</p>
        </div>
        '''
        st.markdown(no_achievements_html, unsafe_allow_html=True)

def update_leaderboard(challenge_type, score, time):
    entry = {
        'username': st.session_state.username,
        'challenge_type': challenge_type,
        'score': score,
        'time': time,
        'timestamp': pd.Timestamp.now()
    }
    st.session_state.leaderboard.append(entry)

def check_achievements():
    # Check for various achievements
    achievements_to_check = [
        ("🎯 First Correct Answer", st.session_state.correct_answers >= 1),
        ("🔥 5 Correct Answers", st.session_state.correct_answers >= 5),
        ("💯 Perfect Score", st.session_state.quiz_score == len(QUIZ_QUESTIONS)),
        ("⚡ Speed Demon", st.session_state.user_score >= 100),
        ("🧠 Knowledge Seeker", st.session_state.quiz_attempts >= 10),
    ]
    
    for achievement, condition in achievements_to_check:
        if condition and achievement not in st.session_state.achievements:
            st.session_state.achievements.append(achievement)
            st.success(f"🎉 Achievement Unlocked: {achievement}")
            st.balloons()

# Data Structure Comparison section
def memory_management():
    st.title("💾 Memory Management")
    save_progress("Memory Mgmt")
    
    st.header("1. Garbage Collection")
    st.markdown("""
    **Automatic Memory Management:**
    - Python, Java, C# automatically free unused nodes
    - Circular references can cause memory leaks
    - GC overhead affects performance
    """)
    
    st.code("""
# Python - Automatic GC
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Memory freed automatically
node = Node(10)
node = None  # Node eligible for GC
    """, language="python")
    
    st.header("2. Memory Leak Prevention")
    st.markdown("""
    **Common Leak Scenarios:**
    - Circular references
    - Lost head pointer
    - Exception during insertion
    - Incomplete deletion
    """)
    
    st.code("""
// C - Manual memory management
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

void deleteList(Node* head) {
    while (head) {
        Node* temp = head;
        head = head->next;
        free(temp);  // Must manually free
    }
}
    """, language="c")
    
    st.header("3. Stack vs Heap Allocation")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Stack")
        st.markdown("""
        - Fast allocation
        - Limited size
        - Automatic cleanup
        - LIFO order
        """)
    
    with col2:
        st.subheader("Heap")
        st.markdown("""
        - Slower allocation
        - Large size
        - Manual/GC cleanup
        - Random access
        """)

def concurrent_linked_lists():
    st.title("🔒 Concurrent Linked Lists")
    save_progress("Concurrency")
    
    st.header("1. Race Conditions")
    st.markdown("""
    **Race conditions** occur when multiple threads access shared data simultaneously.
    """)
    
    st.code("""
# Unsafe linked list operations
class UnsafeLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Race condition!
        self.head = new_node       # Race condition!
    """, language="python")
    
    st.header("2. Lock-Free Implementations")
    st.markdown("""
    **Compare-and-Swap (CAS)** operations enable lock-free programming.
    """)
    
    st.code("""
# Lock-free insertion using CAS
class LockFreeLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        
        while True:
            current_head = self.head
            new_node.next = current_head
            
            # Atomic compare-and-swap
            if self._cas(self.head, current_head, new_node):
                break  # Success!
    """, language="python")
    
    st.header("3. Atomic Operations")
    st.markdown("""
    **Types of Atomic Operations:**
    - Compare-and-Swap (CAS)
    - Fetch-and-Add
    - Load-Link/Store-Conditional
    - Memory Barriers
    """)
    
    st.code("""
// Java - Using AtomicReference
import java.util.concurrent.atomic.AtomicReference;

class LockFreeStack<T> {
    private final AtomicReference<Node<T>> head = new AtomicReference<>();
    
    public void push(T item) {
        Node<T> newNode = new Node<>(item);
        Node<T> currentHead;
        
        do {
            currentHead = head.get();
            newNode.next = currentHead;
        } while (!head.compareAndSet(currentHead, newNode));
    }
}
    """, language="java")

def specialized_linked_lists():
    st.title("🎆 Specialized Linked Lists")
    save_progress("Specialized")
    
    st.header("1. Skip Lists")
    st.markdown("""
    **Skip Lists** are probabilistic data structures that allow O(log n) search time.
    """)
    
    st.code("""
class SkipListNode:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.level = 0
        self.header = SkipListNode(-1, None, max_level)
    
    def search(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while (current.forward[i] and 
                   current.forward[i].key < key):
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return current.value
        return None
    """, language="python")
    
    st.header("2. Self-Organizing Lists")
    st.markdown("""
    **Self-Organizing Lists** automatically rearrange elements based on access patterns.
    """)
    
    st.code("""
class SelfOrganizingList:
    def __init__(self, strategy='mtf'):
        self.head = None
        self.strategy = strategy
    
    def search(self, key):
        if self.head and self.head.data == key:
            return self.head
        
        prev = self.head
        current = self.head.next if self.head else None
        
        while current:
            if current.data == key:
                if self.strategy == 'mtf':  # Move to front
                    prev.next = current.next
                    current.next = self.head
                    self.head = current
                return current
            prev = current
            current = current.next
        return None
    """, language="python")
    
    st.header("3. Unrolled Linked Lists")
    st.markdown("""
    **Unrolled Linked Lists** store multiple elements in each node for better cache performance.
    """)
    
    st.code("""
class UnrolledNode:
    def __init__(self, max_size=4):
        self.max_size = max_size
        self.elements = []
        self.next = None

class UnrolledLinkedList:
    def __init__(self, max_node_size=4):
        self.head = None
        self.max_node_size = max_node_size
    
    def insert(self, index, value):
        # Find appropriate node and insert
        current = self.head
        if not current or len(current.elements) < self.max_node_size:
            if not current:
                self.head = UnrolledNode(self.max_node_size)
                current = self.head
            current.elements.append(value)
    """, language="python")

def real_world_optimizations():
    st.title("🚀 Real-World Optimizations")
    save_progress("Optimizations")
    
    st.header("1. Language-Specific Optimizations")
    
    tab1, tab2, tab3 = st.tabs(["Python", "Java", "C++"])
    
    with tab1:
        st.subheader("Python Optimizations")
        st.code("""
# Use __slots__ to reduce memory
class OptimizedNode:
    __slots__ = ['data', 'next']
    
    def __init__(self, data):
        self.data = data
        self.next = None

# Use collections.deque for better performance
from collections import deque
fast_list = deque()  # O(1) operations at both ends
        """, language="python")
    
    with tab2:
        st.subheader("Java Optimizations")
        st.code("""
// Use generics and size tracking
public class OptimizedLinkedList<T> {
    private Node<T> head;
    private int size;  // O(1) size() method
    
    private static class Node<T> {
        T data;
        Node<T> next;
        Node(T data) { this.data = data; }
    }
    
    public int size() { return size; }
}
        """, language="java")
    
    with tab3:
        st.subheader("C++ Optimizations")
        st.code("""
// Use smart pointers and move semantics
#include <memory>

template<typename T>
class ModernLinkedList {
    struct Node {
        T data;
        std::unique_ptr<Node> next;
        
        template<typename U>
        Node(U&& value) : data(std::forward<U>(value)) {}
    };
    
    std::unique_ptr<Node> head;
    
public:
    void push_front(T&& value) {
        auto new_node = std::make_unique<Node>(std::move(value));
        new_node->next = std::move(head);
        head = std::move(new_node);
    }
};
        """, language="cpp")
    
    st.header("2. Compiler Optimizations")
    st.markdown("""
    **Key Compiler Optimizations:**
    - **Inlining**: Small functions get inlined
    - **Loop Unrolling**: Reduces iteration overhead
    - **Prefetching**: Predicts memory access patterns
    - **Vectorization**: SIMD instructions for parallel operations
    """)
    
    st.header("3. Cache-Friendly Implementations")
    st.markdown("""
    **Cache Optimization Strategies:**
    - **Memory Pools**: Allocate from contiguous memory
    - **Node Packing**: Store multiple small nodes together
    - **Prefetching**: Load next nodes before needed
    - **Data Layout**: Arrange frequently accessed data together
    """)
    
    st.code("""
// Cache-friendly implementation with memory pool
template<typename T>
class CacheFriendlyList {
    struct Node {
        T data;
        size_t next_index;  // Index instead of pointer
    };
    
    std::vector<Node> node_pool;  // Contiguous memory
    size_t head_index;
    
public:
    void traverse_with_prefetch() {
        size_t current = head_index;
        while (current != INVALID_INDEX) {
            size_t next = node_pool[current].next_index;
            if (next != INVALID_INDEX) {
                __builtin_prefetch(&node_pool[next], 0, 1);
            }
            process_data(node_pool[current].data);
            current = next;
        }
    }
};
    """, language="cpp")

def advanced_problem_patterns():
    st.title("🧩 Advanced Problem Patterns")
    save_progress("Patterns")
    
    st.header("1. Two-Pointer Technique Variations")
    st.code("""
# Fast & Slow Pointer - Cycle Detection
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Distance Pointers - Remove Nth from End
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy
    
    for i in range(n + 1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next
    """, language="python")
    
    st.header("2. Sliding Window on Linked Lists")
    st.code("""
# Maximum Sum Sublist of Size K
def max_sum_sublist(head, k):
    current = head
    window_sum = 0
    
    # First window
    for i in range(k):
        window_sum += current.val
        current = current.next
    
    max_sum = window_sum
    left = head
    
    # Slide window
    while current:
        window_sum = window_sum - left.val + current.val
        max_sum = max(max_sum, window_sum)
        left = left.next
        current = current.next
    
    return max_sum
    """, language="python")
    
    st.header("3. System Design Applications")
    st.code("""
# LRU Cache Implementation
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
    """, language="python")

def interview_preparation():
    st.title("📝 Interview Preparation")
    save_progress("Interview")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #1e3c72; text-align: center; margin-bottom: 1.5rem;">🎯 Master Linked List Interviews</h2>
    <p style="font-size: 1.1em; text-align: center; color: #666; margin-bottom: 1rem;">
    Comprehensive preparation guide with top interview questions, complexity analysis, and expert tips.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interview difficulty selector
    difficulty_filter = st.selectbox("Filter by Difficulty:", ["All", "Easy", "Medium", "Hard"])
    
    st.header("🔥 Top 20 Interview Questions")
    
    interview_questions = [
        {"q": "Reverse a singly linked list iteratively and recursively", "difficulty": "Easy", "companies": ["Google", "Amazon", "Microsoft"], "frequency": "Very High"},
        {"q": "Detect if a linked list has a cycle (Floyd's algorithm)", "difficulty": "Medium", "companies": ["Facebook", "Apple", "Netflix"], "frequency": "Very High"},
        {"q": "Find the middle element of a linked list", "difficulty": "Easy", "companies": ["Amazon", "Google", "Uber"], "frequency": "High"},
        {"q": "Merge two sorted linked lists", "difficulty": "Easy", "companies": ["Microsoft", "Amazon", "Apple"], "frequency": "Very High"},
        {"q": "Remove nth node from end of list", "difficulty": "Medium", "companies": ["Google", "Facebook", "LinkedIn"], "frequency": "High"},
        {"q": "Check if a linked list is palindrome", "difficulty": "Easy", "companies": ["Amazon", "Microsoft", "Adobe"], "frequency": "Medium"},
        {"q": "Find intersection point of two linked lists", "difficulty": "Easy", "companies": ["Google", "Amazon", "Bloomberg"], "frequency": "Medium"},
        {"q": "Remove duplicates from sorted linked list", "difficulty": "Easy", "companies": ["Microsoft", "Apple", "Salesforce"], "frequency": "Medium"},
        {"q": "Add two numbers represented as linked lists", "difficulty": "Medium", "companies": ["Amazon", "Google", "Facebook"], "frequency": "High"},
        {"q": "Clone a linked list with random pointers", "difficulty": "Medium", "companies": ["Microsoft", "Amazon", "Google"], "frequency": "Medium"},
        {"q": "Reverse nodes in k-group", "difficulty": "Hard", "companies": ["Google", "Facebook", "Uber"], "frequency": "Medium"},
        {"q": "Sort a linked list using merge sort", "difficulty": "Medium", "companies": ["Amazon", "Microsoft", "Apple"], "frequency": "Medium"},
        {"q": "Flatten a multilevel doubly linked list", "difficulty": "Medium", "companies": ["Google", "Amazon", "LinkedIn"], "frequency": "Low"},
        {"q": "LRU Cache implementation", "difficulty": "Medium", "companies": ["Amazon", "Google", "Microsoft"], "frequency": "Very High"},
        {"q": "Design a data structure for LFU cache", "difficulty": "Hard", "companies": ["Google", "Facebook", "Twitter"], "frequency": "Medium"},
        {"q": "Implement stack using linked list", "difficulty": "Easy", "companies": ["Amazon", "Microsoft", "Oracle"], "frequency": "Medium"},
        {"q": "Implement queue using linked list", "difficulty": "Easy", "companies": ["Google", "Apple", "Netflix"], "frequency": "Medium"},
        {"q": "Find if linked list is circular", "difficulty": "Easy", "companies": ["Amazon", "Adobe", "Salesforce"], "frequency": "Low"},
        {"q": "Rotate linked list by k positions", "difficulty": "Medium", "companies": ["Microsoft", "Google", "Uber"], "frequency": "Medium"},
        {"q": "Convert binary tree to doubly linked list", "difficulty": "Hard", "companies": ["Google", "Amazon", "Facebook"], "frequency": "Low"}
    ]
    
    filtered_questions = interview_questions if difficulty_filter == "All" else [q for q in interview_questions if q["difficulty"] == difficulty_filter]
    
    for i, item in enumerate(filtered_questions, 1):
        difficulty_color = {"Easy": "#4CAF50", "Medium": "#FF9800", "Hard": "#F44336"}[item["difficulty"]]
        frequency_color = {"Very High": "#E91E63", "High": "#FF5722", "Medium": "#FF9800", "Low": "#9E9E9E"}[item["frequency"]]
        
        st.markdown(f"""
        <div style="border-left: 4px solid {difficulty_color}; padding: 15px; margin: 10px 0; background: rgba(255,255,255,0.05); border-radius: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <strong style="font-size: 1.1em;">{i}. {item['q']}</strong>
                <div>
                    <span style="background: {difficulty_color}; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em; margin-right: 5px;">{item['difficulty']}</span>
                    <span style="background: {frequency_color}; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8em;">{item['frequency']}</span>
                </div>
            </div>
            <div style="font-size: 0.9em; color: #666;">
                <strong>Companies:</strong> {', '.join(item['companies'])}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.header("⚡ Time/Space Complexity Cheat Sheet")
    
    st.markdown("""
    <div class="section-card">
    <h3 style="color: #1e3c72; margin-bottom: 1rem;">📊 Quick Reference Table</h3>
    </div>
    """, unsafe_allow_html=True)
    
    complexity_data = {
        'Operation': ['Insert Beginning', 'Insert End', 'Insert at Position', 'Delete Beginning', 'Delete End', 'Delete by Value', 'Search', 'Access by Index', 'Traversal'],
        'Singly Linked': ['O(1)', 'O(n)', 'O(n)', 'O(1)', 'O(n)', 'O(n)', 'O(n)', 'O(n)', 'O(n)'],
        'Doubly Linked': ['O(1)', 'O(1)*', 'O(n)', 'O(1)', 'O(1)*', 'O(n)', 'O(n)', 'O(n)', 'O(n)'],
        'Array/List': ['O(n)', 'O(1)', 'O(n)', 'O(n)', 'O(1)', 'O(n)', 'O(n)', 'O(1)', 'O(n)'],
        'Space Complexity': ['O(1)', 'O(1)', 'O(1)', 'O(1)', 'O(1)', 'O(1)', 'O(1)', 'O(1)', 'O(1)']
    }
    
    df = pd.DataFrame(complexity_data)
    st.dataframe(df, use_container_width=True)
    st.caption("*With tail pointer maintained")
    
    # Advanced complexity analysis
    st.subheader("🎯 Advanced Complexity Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Memory Overhead:**
        - Singly Linked: 1 pointer + data per node
        - Doubly Linked: 2 pointers + data per node
        - Array: Data only (contiguous)
        
        **Cache Performance:**
        - Arrays: Excellent (sequential access)
        - Linked Lists: Poor (random memory access)
        """)
    
    with col2:
        st.markdown("""
        **When to Use:**
        - **Linked List**: Frequent insertions/deletions at beginning
        - **Array**: Random access, cache performance critical
        - **Doubly Linked**: Bidirectional traversal needed
        """)
    
    st.header("❌ Common Mistakes to Avoid")
    
    mistakes_data = [
        {"mistake": "Not checking for null pointers before dereferencing", "impact": "Runtime Error", "solution": "Always check if (node != null) before accessing node.data or node.next"},
        {"mistake": "Forgetting to update size counter", "impact": "Incorrect size() method", "solution": "Increment/decrement size in all insert/delete operations"},
        {"mistake": "Memory leaks in manual memory management", "impact": "Memory exhaustion", "solution": "Always free() allocated nodes in C/C++"},
        {"mistake": "Off-by-one errors in indexing", "impact": "Wrong element access", "solution": "Carefully handle 0-based vs 1-based indexing"},
        {"mistake": "Not handling empty list edge cases", "impact": "Null pointer exceptions", "solution": "Check if head == null before operations"},
        {"mistake": "Infinite loops in circular lists", "impact": "Program hangs", "solution": "Use proper termination conditions or visited tracking"},
        {"mistake": "Not updating both next and prev in doubly linked lists", "impact": "Broken links", "solution": "Always update both pointers in doubly linked operations"},
        {"mistake": "Losing reference to head node", "impact": "Memory leak", "solution": "Store head reference before modifications"},
        {"mistake": "Not considering single node edge cases", "impact": "Incorrect behavior", "solution": "Test with lists of size 0, 1, and 2"},
        {"mistake": "Incorrect pointer manipulation during deletion", "impact": "Broken list structure", "solution": "Update previous node's next pointer before deleting"}
    ]
    
    for i, mistake in enumerate(mistakes_data, 1):
        impact_color = {"Runtime Error": "#F44336", "Memory exhaustion": "#E91E63", "Incorrect size() method": "#FF9800", "Wrong element access": "#FF5722", "Null pointer exceptions": "#F44336", "Program hangs": "#9C27B0", "Broken links": "#FF9800", "Memory leak": "#E91E63", "Incorrect behavior": "#FF9800", "Broken list structure": "#F44336"}[mistake["impact"]]
        
        st.markdown(f"""
        <div style="border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin: 10px 0; background: #fafafa;">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <span style="color: #F44336; font-size: 1.2em; margin-right: 8px;">❌</span>
                <strong style="color: #333;">{i}. {mistake['mistake']}</strong>
            </div>
            <div style="margin-left: 30px;">
                <div style="margin-bottom: 5px;">
                    <strong>Impact:</strong> <span style="color: {impact_color}; font-weight: bold;">{mistake['impact']}</span>
                </div>
                <div>
                    <strong>Solution:</strong> <span style="color: #4CAF50;">{mistake['solution']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.header("💻 Essential Code Templates")
    
    # Tabbed code examples
    tab1, tab2, tab3, tab4 = st.tabs(["🔄 Reverse List", "🔍 Cycle Detection", "🎯 Find Middle", "🔗 Merge Lists"])
    
    with tab1:
        st.subheader("Reverse Linked List")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Iterative Approach:**")
            st.code("""
def reverse_iterative(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# Time: O(n), Space: O(1)
            """, language="python")
        
        with col2:
            st.markdown("**Recursive Approach:**")
            st.code("""
def reverse_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head

# Time: O(n), Space: O(n)
            """, language="python")
    
    with tab2:
        st.subheader("Cycle Detection (Floyd's Algorithm)")
        st.code("""
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

def find_cycle_start(head):
    if not has_cycle(head):
        return None
    
    slow = fast = head
    
    # Find meeting point
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# Time: O(n), Space: O(1)
        """, language="python")
    
    with tab3:
        st.subheader("Find Middle Element")
        st.code("""
def find_middle(head):
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def find_middle_with_prev(head):
    if not head:
        return None, None
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    return slow, prev

# Time: O(n), Space: O(1)
# Returns middle node (for odd length)
# Returns second middle (for even length)
        """, language="python")
    
    with tab4:
        st.subheader("Merge Two Sorted Lists")
        st.code("""
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 or l2
    
    return dummy.next

def merge_k_lists(lists):
    if not lists:
        return None
    
    while len(lists) > 1:
        merged_lists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_lists(l1, l2))
        
        lists = merged_lists
    
    return lists[0]

# Time: O(n + m), Space: O(1)
        """, language="python")
    
    st.header("🎯 Interview Tips & Strategies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Before Coding:**
        - ✅ Clarify input constraints
        - ✅ Ask about edge cases
        - ✅ Discuss time/space requirements
        - ✅ Confirm expected behavior
        
        **During Implementation:**
        - ✅ Use dummy nodes for simplicity
        - ✅ Draw diagrams on whiteboard
        - ✅ Handle null pointers carefully
        - ✅ Test with small examples
        """)
    
    with col2:
        st.markdown("""
        **Common Patterns:**
        - 🔄 Two pointers (fast/slow)
        - 🎯 Dummy head node
        - 📝 Recursive solutions
        - 🔗 Multiple pass algorithms
        
        **Testing Strategy:**
        - 🧪 Empty list (null)
        - 🧪 Single node
        - 🧪 Two nodes
        - 🧪 Odd/even length lists
        """)
    
    # Interactive practice section
    st.header("🏋️ Practice Session")
    
    if st.button("🎯 Start Practice Interview"):
        practice_question = random.choice(filtered_questions)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; padding: 2rem; margin: 1rem 0;">
            <h3>🎯 Practice Question</h3>
            <p style="font-size: 1.2em; margin: 1rem 0;"><strong>{practice_question['q']}</strong></p>
            <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                <span style="background: rgba(255,255,255,0.2); padding: 5px 10px; border-radius: 15px;">Difficulty: {practice_question['difficulty']}</span>
                <span style="background: rgba(255,255,255,0.2); padding: 5px 10px; border-radius: 15px;">Frequency: {practice_question['frequency']}</span>
            </div>
            <p style="margin-top: 1rem; font-size: 0.9em;">💡 Take 5 minutes to think through the approach before coding!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Company-specific preparation
    st.header("🏢 Company-Specific Preparation")
    
    company_focus = {
        "Google": ["Algorithm optimization", "Clean code", "Edge case handling", "Time/space analysis"],
        "Amazon": ["Leadership principles", "Scalability", "Customer obsession", "Operational excellence"],
        "Microsoft": ["Problem-solving approach", "Collaboration", "Technical depth", "System design"],
        "Facebook/Meta": ["Move fast mentality", "Impact focus", "Technical rigor", "Product thinking"],
        "Apple": ["Attention to detail", "User experience", "Performance optimization", "Quality focus"]
    }
    
    selected_company = st.selectbox("Select Company:", list(company_focus.keys()))
    
    st.markdown(f"""
    **{selected_company} Interview Focus:**
    """)
    
    for focus_area in company_focus[selected_company]:
        st.markdown(f"- 🎯 {focus_area}")
    
    # Practice Problems Section
    st.header("📝 Practice Problems with Solutions")
    
    practice_problems = [
        {
            "title": "Add Two Numbers",
            "difficulty": "Medium",
            "description": "You are given two non-empty linked lists representing two non-negative integers. Add the two numbers and return the sum as a linked list.",
            "example": "Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)\nOutput: 7 -> 0 -> 8\nExplanation: 342 + 465 = 807",
            "solution": """def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next"""
        },
        {
            "title": "Remove Nth Node From End",
            "difficulty": "Medium",
            "description": "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
            "example": "Input: head = [1,2,3,4,5], n = 2\nOutput: [1,2,3,5]",
            "solution": """def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy
    
    # Move first n+1 steps ahead
    for i in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node
    second.next = second.next.next
    return dummy.next"""
        },
        {
            "title": "Palindrome Linked List",
            "difficulty": "Easy",
            "description": "Given the head of a singly linked list, return true if it is a palindrome.",
            "example": "Input: head = [1,2,2,1]\nOutput: true",
            "solution": """def isPalindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    
    # Compare halves
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    
    return True"""
        },
        {
            "title": "Intersection of Two Linked Lists",
            "difficulty": "Easy",
            "description": "Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.",
            "example": "Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]\nOutput: Reference to node with value = 8",
            "solution": """def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA"""
        },
        {
            "title": "Copy List with Random Pointer",
            "difficulty": "Medium",
            "description": "A linked list is given such that each node contains an additional random pointer. Return a deep copy of the list.",
            "example": "Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]\nOutput: [[7,null],[13,0],[11,4],[10,2],[1,0]]",
            "solution": """def copyRandomList(head):
    if not head:
        return None
    
    # Create new nodes
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Set random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Separate lists
    dummy = Node(0)
    copy_current = dummy
    current = head
    
    while current:
        copy_current.next = current.next
        current.next = current.next.next
        copy_current = copy_current.next
        current = current.next
    
    return dummy.next"""
        }
    ]
    
    for i, problem in enumerate(practice_problems, 1):
        difficulty_color = {"Easy": "#4CAF50", "Medium": "#FF9800", "Hard": "#F44336"}[problem["difficulty"]]
        
        with st.expander(f"{i}. {problem['title']} ({problem['difficulty']})"):
            st.markdown(f"**Problem:** {problem['description']}")
            st.markdown(f"**Example:**\n```\n{problem['example']}\n```")
            st.code(problem['solution'], language="python")
    
    # Final preparation checklist
    st.header("✅ Final Preparation Checklist")
    
    checklist_items = [
        "Master the top 10 most frequent questions",
        "Practice coding without IDE/autocomplete",
        "Time yourself on each problem (20-30 minutes)",
        "Explain your approach out loud",
        "Handle all edge cases systematically",
        "Optimize for both time and space complexity",
        "Review company-specific interview formats",
        "Prepare questions to ask the interviewer",
        "Practice on whiteboard or paper",
        "Mock interview with peers or mentors"
    ]
    
    for item in checklist_items:
        st.markdown(f"☐ {item}")
    
    st.success("🚀 You're ready to ace your linked list interviews! Good luck!")

def testing_and_debugging():
    st.markdown('''
    <div class="section-card">
        <h2 style="background: linear-gradient(135deg, var(--error-red), var(--warning-orange)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-align: center; margin-bottom: 2rem;">
            🧪 Testing & Debugging
        </h2>
    </div>
    ''', unsafe_allow_html=True)
    save_progress("Testing")
    
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--text-primary); margin: 0 0 1rem 0;">1. Unit Testing Strategies</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    test_code_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--primary-blue);">📝</span>
            <h4 style="color: var(--text-primary); margin: 0;">Pytest Implementation</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code># Using pytest for linked list testing
import pytest
from linked_list import LinkedList, Node

class TestLinkedList:
    def setup_method(self):
        self.ll = LinkedList()
    
    def test_empty_list(self):
        assert self.ll.size == 0
        assert self.ll.head is None
    
    def test_insert_single_element(self):
        self.ll.insert_at_beginning(10)
        assert self.ll.size == 1
        assert self.ll.head.data == 10
    
    def test_edge_cases(self):
        assert self.ll.delete_from_beginning() is None
        assert self.ll.search(10) == -1</code></pre>
    </div>
    '''
    st.markdown(test_code_html, unsafe_allow_html=True)
    
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--text-primary); margin: 0 0 1rem 0;">2. Memory Debugging Tools</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    memory_code_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--warning-orange);">🧠</span>
            <h4 style="color: var(--text-primary); margin: 0;">Memory Profiling</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code># Python memory profiling
from memory_profiler import profile

@profile
def test_memory_usage():
    ll = LinkedList()
    for i in range(10000):
        ll.insert_at_end(i)
    while ll.size > 0:
        ll.delete_from_beginning()
    return ll

# Run with: python -m memory_profiler test_memory.py</code></pre>
    </div>
    '''
    st.markdown(memory_code_html, unsafe_allow_html=True)
    
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--text-primary); margin: 0 0 1rem 0;">3. Performance Profiling</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    perf_code_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--success-green);">⚡</span>
            <h4 style="color: var(--text-primary); margin: 0;">Performance Analysis</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code># Profile linked list operations
import cProfile
import pstats

def profile_operations():
    ll = LinkedList()
    for i in range(10000):
        ll.insert_at_end(i)
    for i in range(100):
        ll.search(i * 100)

if __name__ == "__main__":
    cProfile.run('profile_operations()', 'results.prof')
    stats = pstats.Stats('results.prof')
    stats.sort_stats('cumulative')
    stats.print_stats(10)</code></pre>
    </div>
    '''
    st.markdown(perf_code_html, unsafe_allow_html=True)
    
    if st.button("🐛 Run Debug Session"):
        st.success("🎉 Debug session completed successfully!")

def integration_topics():
    st.markdown('''
    <div style="background: linear-gradient(135deg, var(--primary-purple), var(--primary-blue)); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5rem;">🔗 Integration Topics</h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin: 0.5rem 0 0 0;">Real-world applications of linked lists</p>
    </div>
    ''', unsafe_allow_html=True)
    save_progress("Integration")
    
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">1. Linked Lists in Databases</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    db_buffer_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--info-blue);">💾</span>
            <h4 style="color: var(--text-primary); margin: 0;">Database Buffer Pool with LRU</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code># Database Buffer Pool with LRU
class BufferPool:
    def __init__(self, size):
        self.size = size
        self.pages = {}
        self.head = PageNode(None, None)
        self.tail = PageNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get_page(self, page_id):
        if page_id in self.pages:
            node = self.pages[page_id]
            self._move_to_front(node)
            return node.data
        
        page_data = self._load_from_disk(page_id)
        
        if len(self.pages) >= self.size:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.pages[lru_node.page_id]
        
        new_node = PageNode(page_id, page_data)
        self._add_to_front(new_node)
        self.pages[page_id] = new_node
        
        return page_data</code></pre>
    </div>
    '''
    st.markdown(db_buffer_html, unsafe_allow_html=True)
    
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">2. File System Implementations</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    file_system_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--success-green);">📁</span>
            <h4 style="color: var(--text-primary); margin: 0;">File Allocation Table</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code># File Allocation Table
class FileAllocationTable:
    def __init__(self, total_clusters):
        self.total_clusters = total_clusters
        self.fat = [0] * total_clusters
        self.free_clusters = list(range(1, total_clusters))
    
    def allocate_file(self, file_size_clusters):
        if len(self.free_clusters) < file_size_clusters:
            return None
        
        allocated = []
        for i in range(file_size_clusters):
            cluster = self.free_clusters.pop(0)
            allocated.append(cluster)
            
            if i == file_size_clusters - 1:
                self.fat[cluster] = -1
            else:
                self.fat[cluster] = self.free_clusters[0]
        
        return allocated[0]</code></pre>
    </div>
    '''
    st.markdown(file_system_html, unsafe_allow_html=True)
    
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">3. Network Packet Handling</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    network_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--warning-orange);">🌐</span>
            <h4 style="color: var(--text-primary); margin: 0;">Network Packet Queue with Priority</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code># Network Packet Queue with Priority
class PacketQueue:
    def __init__(self):
        self.high_priority = None
        self.normal_priority = None
        self.low_priority = None
    
    def enqueue(self, packet):
        new_node = PacketNode(packet)
        
        if packet.priority == 'high':
            new_node.next = self.high_priority
            self.high_priority = new_node
        elif packet.priority == 'normal':
            new_node.next = self.normal_priority
            self.normal_priority = new_node
        else:
            new_node.next = self.low_priority
            self.low_priority = new_node
    
    def dequeue(self):
        if self.high_priority:
            packet = self.high_priority.packet
            self.high_priority = self.high_priority.next
            return packet
        
        if self.normal_priority:
            packet = self.normal_priority.packet
            self.normal_priority = self.normal_priority.next
            return packet
        
        if self.low_priority:
            packet = self.low_priority.packet
            self.low_priority = self.low_priority.next
            return packet
        
        return None</code></pre>
    </div>
    '''
    st.markdown(network_html, unsafe_allow_html=True)

def data_structure_comparison():
    st.markdown('''
    <div style="background: linear-gradient(135deg, var(--primary-purple), var(--primary-blue)); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5rem;">📊 Data Structure Comparison</h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin: 0.5rem 0 0 0;">Linked Lists vs Arrays - Choose wisely!</p>
    </div>
    ''', unsafe_allow_html=True)
    save_progress("Comparison")

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Linked Lists vs Arrays</h2>
    </div>
    ''', unsafe_allow_html=True)

    comparison_data = {
        'Aspect': [
            'Random Access',
            'Insertion at Beginning',
            'Insertion at End',
            'Deletion from Beginning',
            'Deletion from End',
            'Memory Usage',
            'Cache Performance',
            'Implementation Complexity'
        ],
        'Linked List': ['O(n)', 'O(1)', 'O(n)', 'O(1)', 'O(n)', 'Higher', 'Poor', 'Moderate'],
        'Dynamic Array': ['O(1)', 'O(n)', 'O(1)*', 'O(n)', 'O(1)', 'Lower', 'Excellent', 'Simple']
    }

    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)

    st.markdown("*Note: * Amortized O(1) for dynamic arrays")

    # Interactive comparison chart
    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Performance Comparison Chart</h2>
    </div>
    ''', unsafe_allow_html=True)

    aspects = ['Random Access', 'Insert Beginning', 'Insert End', 'Delete Beginning', 'Delete End']
    linked_list_scores = [10, 1, 10, 1, 10]  # Lower is better
    array_scores = [1, 10, 1, 10, 1]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Linked List',
        x=aspects,
        y=linked_list_scores,
        marker_color='#1e3c72'
    ))

    fig.add_trace(go.Bar(
        name='Dynamic Array',
        x=aspects,
        y=array_scores,
        marker_color='#667eea'
    ))

    fig.update_layout(
        title="Performance Comparison (Lower is Better)",
        barmode='group',
        yaxis_title="Complexity Score",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">When to Use Which?</h2>
    </div>
    ''', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
        <div style="background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(76, 175, 80, 0.05)); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(76, 175, 80, 0.3);">
            <h3 style="color: var(--success-green); margin: 0 0 1rem 0;">Choose Linked List when:</h3>
            <ul style="color: var(--text-primary); margin: 0; padding-left: 1.5rem;">
                <li>✅ Frequent insertions/deletions at beginning</li>
                <li>✅ Dynamic size requirements</li>
                <li>✅ Memory allocation/deallocation is expensive</li>
                <li>✅ Implementing stacks, queues, or graphs</li>
                <li>✅ Sequential access patterns</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
        <div style="background: linear-gradient(135deg, rgba(33, 150, 243, 0.1), rgba(33, 150, 243, 0.05)); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(33, 150, 243, 0.3);">
            <h3 style="color: var(--info-blue); margin: 0 0 1rem 0;">Choose Array when:</h3>
            <ul style="color: var(--text-primary); margin: 0; padding-left: 1.5rem;">
                <li>✅ Need fast random access</li>
                <li>✅ Memory efficiency is critical</li>
                <li>✅ Most operations are at the end</li>
                <li>✅ Simple implementation needed</li>
                <li>✅ Cache performance matters</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Linked Lists vs Other Data Structures</h2>
    </div>
    ''', unsafe_allow_html=True)

    structures = ['Linked List', 'Array', 'Stack', 'Queue', 'Tree', 'Graph']
    use_cases = [
        'Dynamic sequences, undo operations',
        'Static sequences, fast access',
        'LIFO operations, function calls',
        'FIFO operations, scheduling',
        'Hierarchical data, searching',
        'Complex relationships, networks'
    ]

    comparison_df = pd.DataFrame({
        'Data Structure': structures,
        'Primary Use Cases': use_cases
    })

    st.dataframe(comparison_df, use_container_width=True)

# Advanced Algorithms section
def advanced_algorithms():
    st.markdown('''
    <div style="background: linear-gradient(135deg, var(--primary-purple), var(--primary-blue)); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5rem;">🚀 Advanced Algorithms</h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin: 0.5rem 0 0 0;">Master complex linked list operations</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Merge Sort on Linked Lists</h2>
        <div style="background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 193, 7, 0.05)); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; margin: 1rem 0; border: 1px solid rgba(255, 193, 7, 0.3);">
            <h4 style="color: var(--warning-orange); margin: 0 0 0.5rem 0;">Why Merge Sort for Linked Lists?</h4>
            <ul style="color: var(--text-primary); margin: 0; padding-left: 1.5rem;">
                <li>Linked lists don't support random access</li>
                <li>Merge sort is efficient for linked structures</li>
                <li>No extra space needed for merging</li>
                <li>Stable sorting algorithm</li>
            </ul>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    merge_sort_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--success-green);">⚡</span>
            <h4 style="color: var(--text-primary); margin: 0;">Merge Sort Implementation</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code>def merge_sort(head):
    if not head or not head.next:
        return head

    # Find middle of list
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list
    middle = slow.next
    slow.next = None

    # Recursively sort both halves
    left = merge_sort(head)
    right = merge_sort(middle)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

# Time Complexity: O(n log n)
# Space Complexity: O(log n) for recursion stack</code></pre>
    </div>
    '''
    st.markdown(merge_sort_html, unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Quick Sort on Linked Lists</h2>
    </div>
    ''', unsafe_allow_html=True)

    quick_sort_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--warning-orange);">🔥</span>
            <h4 style="color: var(--text-primary); margin: 0;">Quick Sort Implementation</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code>def quick_sort(head):
    if not head or not head.next:
        return head

    # Partition around pivot
    pivot = head
    smaller_head = None
    smaller_tail = None
    greater_head = None
    greater_tail = None

    current = head.next

    while current:
        if current.data < pivot.data:
            if not smaller_head:
                smaller_head = current
                smaller_tail = current
            else:
                smaller_tail.next = current
                smaller_tail = current
        else:
            if not greater_head:
                greater_head = current
                greater_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
        current = current.next

    # Terminate partitions properly
    if smaller_tail:
        smaller_tail.next = None
    if greater_tail:
        greater_tail.next = None
        
    # Recursively sort partitions
    smaller_sorted = quick_sort(smaller_head)
    greater_sorted = quick_sort(greater_head)

    # Connect all parts
    if smaller_tail:
        smaller_tail.next = pivot
    else:
        smaller_head = pivot

    pivot.next = greater_sorted

    return smaller_head if smaller_head else pivot

# Time Complexity: O(n²) worst case, O(n log n) average
# Space Complexity: O(log n) for recursion stack</code></pre>
    </div>
    '''
    st.markdown(quick_sort_html, unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Cycle Detection Algorithms</h2>
    </div>
    ''', unsafe_allow_html=True)

    floyd_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--info-blue);">🐢🐇</span>
            <h4 style="color: var(--text-primary); margin: 0;">Floyd's Cycle Detection Algorithm</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code>def detect_cycle_floyd(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Time Complexity: O(n)
# Space Complexity: O(1)</code></pre>
    </div>
    '''
    st.markdown(floyd_html, unsafe_allow_html=True)

    brent_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--warning-orange);">🔍</span>
            <h4 style="color: var(--text-primary); margin: 0;">Brent's Cycle Detection Algorithm</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code>def detect_cycle_brent(head):
    if not head:
        return False

    slow = head
    fast = head.next
    power = 1
    length = 1

    # Find cycle
    while fast and fast != slow:
        if power == length:
            power *= 2
            length = 0
            slow = fast

        fast = fast.next
        length += 1

    return fast is not None

# Time Complexity: O(n)
# Space Complexity: O(1)
# Often faster than Floyd's algorithm in practice</code></pre>
    </div>
    '''
    st.markdown(brent_html, unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Advanced Operations</h2>
    </div>
    ''', unsafe_allow_html=True)

    reverse_groups_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span style="color: var(--success-green);">🔄</span>
            <h4 style="color: var(--text-primary); margin: 0;">Reverse k nodes at a time</h4>
        </div>
        <pre style="color: var(--text-primary); overflow-x: auto;"><code>def reverse_k_groups(head, k):
    if not head or k == 1:
        return head

    # Count total nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    # Create dummy node
    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy

    while count >= k:
        current = prev_group_end.next
        next_group_start = current

        # Reverse k nodes
        for i in range(k - 1):
            temp = current.next
            current.next = temp.next
            temp.next = prev_group_end.next
            prev_group_end.next = temp

        prev_group_end = next_group_start
        count -= k

    return dummy.next

# Example: reverse_k_groups([1,2,3,4,5], 2) -> [2,1,4,3,5]</code></pre>
    </div>
    '''
    st.markdown(reverse_groups_html, unsafe_allow_html=True)

# Example: reverse_k_groups([1,2,3,4,5], 2) -> [2,1,4,3,5]

# Memory Layout Visualizations section
def memory_layout_visualizations():
    st.markdown('''
    <div style="background: linear-gradient(135deg, var(--primary-purple), var(--primary-blue)); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5rem;">💾 Memory Layout Visualizations</h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin: 0.5rem 0 0 0;">Understanding memory allocation and fragmentation in linked lists</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">How Linked Lists are Stored in Memory</h2>
        <div style="background: linear-gradient(135deg, rgba(14, 165, 233, 0.1), rgba(14, 165, 233, 0.05)); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; margin: 1rem 0; border: 1px solid rgba(14, 165, 233, 0.3);">
            <h4 style="color: var(--info-blue); margin: 0 0 0.5rem 0;">Key Concept</h4>
            <p style="color: var(--text-primary); margin: 0; line-height: 1.7;">Unlike arrays that store elements in contiguous memory locations, linked list nodes are scattered throughout memory and connected via pointers.</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Interactive memory layout demo
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-md);
    ">
        <h3 style="color: var(--primary-700); margin-bottom: 1.5rem;">Interactive Memory Layout</h3>
    """, unsafe_allow_html=True)

    if 'demo_list' not in st.session_state:
        st.session_state.demo_list = [10, 20, 30, 40]

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Memory Blocks")
        memory_placeholder = st.empty()

    with col2:
        st.markdown("### Controls")
        
        # Modern button styling
        st.markdown("""
        <div style="
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        ">
        """, unsafe_allow_html=True)
        
        if st.button("➕ Add Node", help="Add a new node to the linked list"):
            st.session_state.demo_list.append(len(st.session_state.demo_list) * 10 + 10)
            st.rerun()

        if st.button("➖ Remove Node", help="Remove the last node from the linked list") and st.session_state.demo_list:
            st.session_state.demo_list.pop()
            st.rerun()

        if st.button("🔀 Shuffle Memory", help="Randomize the memory layout"):
            import random
            random.shuffle(st.session_state.demo_list)
            st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Display memory layout
    with memory_placeholder.container():
        if st.session_state.demo_list:
            cols = st.columns(min(6, len(st.session_state.demo_list)))

            for i, val in enumerate(st.session_state.demo_list):
                if i < 6:  # Show max 6 blocks
                    with cols[i]:
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, var(--primary-100) 0%, var(--primary-200) 100%);
                            border-radius: var(--radius-lg);
                            padding: 1.5rem;
                            margin: 0.5rem;
                            text-align: center;
                            box-shadow: var(--shadow-md);
                            transition: all var(--transition-normal);
                            border: 1px solid rgba(14, 165, 233, 0.2);
                        " onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow-xl)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-md)'">
                            <div style="font-weight: 600; color: var(--primary-700); margin-bottom: 0.5rem;">Block {i}</div>
                            <div style="font-size: 1.5rem; font-weight: 700; color: var(--primary-800); margin: 1rem 0;">{val}</div>
                            <div style="font-size: 0.9rem; color: var(--primary-600); margin-bottom: 1rem;">Addr: 0x{i*100:03X}</div>
                            {'<div style="font-size: 1.5rem; color: var(--primary-600);">→</div>' if i < len(st.session_state.demo_list) - 1 else '<div style="font-size: 1.5rem; color: var(--error-500);">NULL</div>'}
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.info("Add some nodes to see the memory layout!")
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Memory Fragmentation</h2>
        <div style="background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 193, 7, 0.05)); backdrop-filter: blur(10px); border-radius: 12px; padding: 1rem; margin: 1rem 0; border: 1px solid rgba(255, 193, 7, 0.3);">
            <h4 style="color: var(--warning-orange); margin: 0 0 0.5rem 0;">Memory Fragmentation</h4>
            <p style="color: var(--text-primary); margin: 0; line-height: 1.7;">Memory fragmentation occurs when free memory is divided into small, non-contiguous blocks. This can happen with frequent insertions and deletions in linked lists.</p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Fragmentation visualization
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-md);
    ">
        <h3 style="color: var(--primary-700); margin-bottom: 1.5rem;">Fragmentation Demo</h3>
    """, unsafe_allow_html=True)

    fragmentation_data = [
        {"address": "0x100", "size": 32, "status": "used", "data": "Node A"},
        {"address": "0x120", "size": 16, "status": "free", "data": ""},
        {"address": "0x130", "size": 48, "status": "used", "data": "Node B"},
        {"address": "0x160", "size": 24, "status": "free", "data": ""},
        {"address": "0x184", "size": 40, "status": "used", "data": "Node C"},
    ]

    for block in fragmentation_data:
        bg_color = "rgba(34, 197, 94, 0.1)" if block["status"] == "used" else "rgba(239, 68, 68, 0.1)"
        text_color = "var(--success-600)" if block["status"] == "used" else "var(--error-600)"
        st.markdown(f"""
        <div style="
            display: flex; 
            align-items: center; 
            margin: 0.75rem 0; 
            padding: 1rem; 
            border-radius: var(--radius-md); 
            background: {bg_color};
            border: 1px solid {'rgba(34, 197, 94, 0.2)' if block['status'] == 'used' else 'rgba(239, 68, 68, 0.2)'};
            transition: all var(--transition-normal);
        " onmouseover="this.style.transform='translateX(4px)'; this.style.boxShadow='var(--shadow-sm)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='none'">
            <div style="width: 120px; font-weight: 600; color: var(--primary-700);">{block['address']}</div>
            <div style="width: 80px; color: var(--neutral-600);">{block['size']}B</div>
            <div style="width: 100px; color: {text_color}; font-weight: 600;">{block['status'].upper()}</div>
            <div style="flex: 1; color: var(--neutral-700);">{block['data']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
        <h3 style="color: var(--primary-700); margin-bottom: 1rem;">Impact of Fragmentation</h3>
        <div style="display: grid; gap: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span style="color: var(--error-500); font-size: 1.2rem;">⚠️</span>
                <div>
                    <strong style="color: var(--primary-700);">Memory Waste:</strong>
                    <span style="color: var(--neutral-600);">Small free blocks can't be used for larger allocations</span>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span style="color: var(--warning-500); font-size: 1.2rem;">⚡</span>
                <div>
                    <strong style="color: var(--primary-700);">Performance:</strong>
                    <span style="color: var(--neutral-600);">Increased time for memory allocation/deallocation</span>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span style="color: var(--secondary-500); font-size: 1.2rem;">🔄</span>
                <div>
                    <strong style="color: var(--primary-700);">Cache Issues:</strong>
                    <span style="color: var(--neutral-600);">Scattered memory access patterns</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
        <h2 style="color: var(--primary-700); margin-bottom: 1rem;">Cache Performance</h2>
        <p style="color: var(--neutral-600); line-height: 1.7;">
            <strong>Cache Locality</strong> refers to how closely related data elements are stored in memory.
            Arrays have excellent cache locality, while linked lists have poor cache locality.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Cache performance visualization
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-md);
    ">
        <h3 style="color: var(--primary-700); margin-bottom: 1.5rem;">Cache Access Patterns</h3>
    """, unsafe_allow_html=True)

    cache_demo = st.selectbox("Select data structure:", ["Array", "Linked List"])

    if cache_demo == "Array":
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(22, 163, 74, 0.1) 100%);
            border: 1px solid rgba(34, 197, 94, 0.2);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            margin: 1rem 0;
        ">
            <h4 style="color: var(--success-600); margin-bottom: 1rem;">Array Access Pattern</h4>
            <div style="display: grid; gap: 0.75rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--success-500);">✓</span>
                    <span style="color: var(--neutral-700);">Elements stored contiguously: [10][20][30][40][50]</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--success-500);">✓</span>
                    <span style="color: var(--neutral-700);">Memory addresses: 0x100, 0x104, 0x108, 0x10C, 0x110</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--success-500);">⚡</span>
                    <strong style="color: var(--success-600);">Cache Performance:</strong>
                    <span style="color: var(--neutral-700);">Excellent - sequential access</span>
                </div>
            </div>
        </div>
        """)
    else:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(220, 38, 38, 0.1) 100%);
            border: 1px solid rgba(239, 68, 68, 0.2);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            margin: 1rem 0;
        ">
            <h4 style="color: var(--error-600); margin-bottom: 1rem;">Linked List Access Pattern</h4>
            <div style="display: grid; gap: 0.75rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--error-500);">⚠️</span>
                    <span style="color: var(--neutral-700);">Elements scattered: 10(0x100) → 20(0x200) → 30(0x150) → 40(0x300)</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--error-500);">⚠️</span>
                    <span style="color: var(--neutral-700);">Memory addresses: 0x100, 0x200, 0x150, 0x300</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: var(--error-500);">❌</span>
                    <strong style="color: var(--error-600);">Cache Performance:</strong>
                    <span style="color: var(--neutral-700);">Poor - random access, cache misses</span>
                </div>
            </div>
        </div>
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Performance Benchmarks section
def performance_benchmarks():
    st.markdown('''
    <div style="background: linear-gradient(135deg, var(--primary-purple), var(--primary-blue)); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5rem;">📊 Performance Benchmarks</h1>
        <p style="color: rgba(255,255,255,0.8); text-align: center; margin: 0.5rem 0 0 0;">Compare linked lists vs arrays in real-time</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Actual Timing Comparisons</h2>
    </div>
    ''', unsafe_allow_html=True)

    if st.button("Run Benchmarks"):
        import time

        # Test data sizes
        sizes = [100, 1000, 10000]

        results = {
            'Size': [],
            'Operation': [],
            'Linked List (ms)': [],
            'Array (ms)': []
        }

        for size in sizes:
            # Create test data
            test_data = list(range(size))

            # Linked List Implementation
            class Node:
                def __init__(self, data):
                    self.data = data
                    self.next = None

            class LinkedList:
                def __init__(self):
                    self.head = None

                def insert_at_end(self, data):
                    if not self.head:
                        self.head = Node(data)
                        return
                    current = self.head
                    while current.next:
                        current = current.next
                    current.next = Node(data)

                def search(self, target):
                    current = self.head
                    while current:
                        if current.data == target:
                            return True
                        current = current.next
                    return False

            # Create structures
            ll = LinkedList()
            array = []

            # Insert at end - Linked List
            start_time = time.time()
            for item in test_data:
                ll.insert_at_end(item)
            ll_insert_time = (time.time() - start_time) * 1000

            # Insert at end - Array
            start_time = time.time()
            for item in test_data:
                array.append(item)
            array_insert_time = (time.time() - start_time) * 1000

            # Search - Linked List
            start_time = time.time()
            for _ in range(100):  # Search 100 times
                ll.search(size // 2)
            ll_search_time = (time.time() - start_time) * 1000 / 100

            # Search - Array
            start_time = time.time()
            for _ in range(100):  # Search 100 times
                (size // 2) in array
            array_search_time = (time.time() - start_time) * 1000 / 100

            # Record results
            results['Size'].extend([size, size])
            results['Operation'].extend(['Insert at End', 'Search'])
            results['Linked List (ms)'].extend([ll_insert_time, ll_search_time])
            results['Array (ms)'].extend([array_insert_time, array_search_time])

        # Display results
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)

        # Create comparison chart
        fig = go.Figure()

        for op in ['Insert at End', 'Search']:
            op_data = df[df['Operation'] == op]
            fig.add_trace(go.Bar(
                name=f'Linked List - {op}',
                x=[f"Size {size}" for size in op_data['Size']],
                y=op_data['Linked List (ms)'],
                marker_color='#1e3c72'
            ))
            fig.add_trace(go.Bar(
                name=f'Array - {op}',
                x=[f"Size {size}" for size in op_data['Size']],
                y=op_data['Array (ms)'],
                marker_color='#667eea'
            ))

        fig.update_layout(
            title="Performance Benchmarks",
            barmode='group',
            yaxis_title="Time (milliseconds)",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown('''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h2 style="color: var(--text-primary); margin: 0 0 1rem 0;">Memory Usage Analysis</h2>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("")
    memory_comparison_html = '''
    <div style="background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h4 style="color: var(--text-primary); margin: 0 0 1rem 0;">Memory Overhead Comparison</h4>
        <table style="width: 100%; border-collapse: collapse; color: var(--text-primary);">
            <thead>
                <tr style="background: rgba(255, 255, 255, 0.1);">
                    <th style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2); text-align: left;">Data Structure</th>
                    <th style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2); text-align: left;">Element Size</th>
                    <th style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2); text-align: left;">Overhead</th>
                    <th style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2); text-align: left;">Total per Element</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">Linked List (Python)</td>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">28 bytes</td>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">8 bytes (pointer)</td>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">~36 bytes</td>
                </tr>
                <tr style="background: rgba(255, 255, 255, 0.05);">
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">Dynamic Array (Python)</td>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">28 bytes</td>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">~4 bytes (amortized)</td>
                    <td style="padding: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.2);">~32 bytes</td>
                </tr>
            </tbody>
        </table>
        <div style="background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 193, 7, 0.05)); backdrop-filter: blur(10px); border-radius: 8px; padding: 0.75rem; margin-top: 1rem; border: 1px solid rgba(255, 193, 7, 0.3);">
            <p style="color: var(--warning-orange); margin: 0; font-size: 0.9rem;">Note: Actual memory usage depends on the programming language and implementation.</p>
        </div>
    </div>
    '''
    st.markdown(memory_comparison_html, unsafe_allow_html=True)

# Progress Tracking Feature
def save_progress(section_name, data=None):
    """Save user progress"""
    st.session_state.progress_data[section_name] = {
        'completed': True,
        'timestamp': pd.Timestamp.now(),
        'data': data
    }
    st.session_state.completed_sections.add(section_name)

def get_progress_percentage():
    """Calculate overall progress"""
    total_sections = 10
    return (len(st.session_state.completed_sections) / total_sections) * 100

# Search Feature
def search_content(query):
    """Global search functionality with suggestions"""
    search_data = {
        'Introduction': ['linked', 'list', 'node', 'pointer', 'memory', 'data', 'structure', 'intro'],
        'Types': ['singly', 'doubly', 'circular', 'XOR', 'skip', 'list', 'type'],
        'Operations': ['insert', 'delete', 'search', 'traverse', 'reverse', 'operation', 'algo'],
        'Playground': ['interactive', 'visualization', 'create', 'modify', 'play', 'demo'],
        'Analysis': ['performance', 'complexity', 'time', 'space', 'benchmark', 'compare'],
        'Practice': ['problems', 'solutions', 'algorithms', 'coding', 'exercise'],
        'Quiz': ['questions', 'test', 'knowledge', 'game', 'challenge'],
        'Comparison': ['array', 'vs', 'memory', 'cache', 'efficiency', 'compare', 'diff'],
        'Testing': ['unit', 'test', 'debug', 'memory', 'profile', 'benchmark'],
        'Interview': ['questions', 'complexity', 'mistakes', 'preparation', 'coding', 'companies', 'tips', 'practice', 'solutions'],
        'Sum': ['calculate', 'total', 'addition', 'examples', 'practice', 'algorithm'],
        'Memory': ['garbage', 'collection', 'leak', 'stack', 'heap', 'allocation'],
        'Concurrency': ['thread', 'safe', 'lock', 'atomic', 'race', 'condition'],
        'Specialized': ['skip', 'list', 'self', 'organizing', 'unrolled', 'advanced'],
        'Optimizations': ['compiler', 'cache', 'language', 'performance', 'optimization'],
        'Patterns': ['two', 'pointer', 'sliding', 'window', 'system', 'design'],
        'Integration': ['database', 'file', 'system', 'network', 'packet', 'handling']
    }
    
    if query:
        query = query.lower().strip()
        results = []
        for section, keywords in search_data.items():
            # Check section name contains query
            if query in section.lower():
                results.append(section)
            # Check keywords contain query
            elif any(query in keyword for keyword in keywords):
                results.append(section)
        return list(set(results))  # Remove duplicates
    return []

def get_search_suggestions(query):
    """Get search suggestions based on input"""
    all_terms = ['Introduction', 'Types', 'Operations', 'Playground', 'Analysis', 'Practice', 'Quiz', 'Comparison', 'complexity', 'performance', 'insert', 'delete', 'node', 'pointer', 'linked', 'list', 'array', 'memory']
    
    query_lower = query.lower()
    # First try starts with, then contains
    starts_with = [term for term in all_terms if term.lower().startswith(query_lower)]
    contains = [term for term in all_terms if query_lower in term.lower() and term not in starts_with]
    suggestions = starts_with + contains
    return suggestions[:4]

# Code Export Feature
def export_code(code_content, filename="linked_list_code.py"):
    """Export code functionality"""
    return st.download_button(
        label="📥 Download Code",
        data=code_content,
        file_name=filename,
        mime="text/plain"
    )

# Step-by-Step Visualization
def step_by_step_insert(elements, new_value, position):
    """Animated insertion visualization"""
    steps = []
    if position == 0:  # Insert at beginning
        steps = [
            f"Step 1: Create new node with value {new_value}",
            "Step 2: Set new node's next to current head",
            "Step 3: Update head to point to new node",
            "Step 4: Insertion complete!"
        ]
    else:  # Insert at end
        steps = [
            f"Step 1: Create new node with value {new_value}",
            "Step 2: Traverse to the last node",
            "Step 3: Set last node's next to new node",
            "Step 4: Insertion complete!"
        ]
    return steps

# New Features
def add_bookmark(section_name):
    if section_name not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(section_name)
        st.success(f"📌 Bookmarked {section_name}!")

def save_note(section_name, note_text):
    st.session_state.notes[section_name] = {'text': note_text, 'timestamp': pd.Timestamp.now()}
    st.success("📝 Note saved!")

def get_study_time():
    st.session_state.study_time += 0.1  # Increment study time
    return st.session_state.study_time

# Mobile Responsive CSS
def mobile_responsive_css():
    """Add mobile responsive styles"""
    css_content = r"""
    <style>
    @media (max-width: 768px) {
        .main-header { font-size: 2rem !important; }
        .section-card { padding: 1rem !important; margin: 0.5rem 0 !important; }
        .feature-card { padding: 1rem !important; margin: 0.25rem !important; }
        .stColumns { flex-direction: column !important; }
        .quiz-container { padding: 1rem !important; }
    }
    </style>
    """
    st.markdown(css_content, unsafe_allow_html=True)

# Theme Toggle Feature
def theme_toggle():
    """Add dark/light theme toggle functionality"""
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    
    # Apply theme
    theme_class = "dark" if st.session_state.dark_mode else "light"
    st.markdown(f'<div data-theme="{theme_class}" style="min-height: 100vh;">', unsafe_allow_html=True)
    
    # Dynamic theme CSS
    if st.session_state.dark_mode:
        dark_css = """
        <style>
            .stApp {
                background: #1a1a1a !important;
                color: #e0e0e0 !important;
            }
            
            .main .block-container {
                background: #1a1a1a !important;
            }
            
            .stApp > div {
                background: #1a1a1a !important;
            }
            
            div[data-testid="stSidebar"] {
                background: #2d2d2d !important;
            }
            
            .section-card {
                background: #2d2d2d !important;
                border-left: 6px solid #64b5f6 !important;
                color: #e0e0e0 !important;
            }
            
            .feature-card {
                background: linear-gradient(135deg, #424242 0%, #616161 100%) !important;
            }
            
            .interactive-card {
                background: linear-gradient(135deg, #37474f 0%, #455a64 100%) !important;
            }
            
            .code-block {
                background: #1e1e1e !important;
                border-left: 4px solid #64b5f6 !important;
                color: #e0e0e0 !important;
            }
            
            .visual-diagram {
                background: #2c2c2c !important;
                color: #e0e0e0 !important;
            }
            
            .metric-card {
                background: linear-gradient(135deg, #37474f 0%, #455a64 100%) !important;
            }
            
            .quiz-container {
                background: linear-gradient(135deg, #37474f 0%, #455a64 100%) !important;
            }
            
            .stMarkdown {
                color: #e0e0e0 !important;
            }
            
            .stDataFrame {
                background: #2d2d2d !important;
            }
            
            .stPlotlyChart {
                background: #2d2d2d !important;
            }
        </style>
        """
        st.markdown(dark_css, unsafe_allow_html=True)
    else:
        light_css = """
        <style>
            .stApp {
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
            }
        </style>
        """
        st.markdown(light_css, unsafe_allow_html=True)

# Main app function
def main():
    # Initialize session state for tab navigation
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = 0

    # Initialize gamification session state
    if 'user_score' not in st.session_state:
        st.session_state.user_score = 0
    if 'quiz_attempts' not in st.session_state:
        st.session_state.quiz_attempts = 0
    if 'correct_answers' not in st.session_state:
        st.session_state.correct_answers = 0
    if 'leaderboard' not in st.session_state:
        st.session_state.leaderboard = []
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []
    if 'current_challenge' not in st.session_state:
        st.session_state.current_challenge = None
    if 'challenge_start_time' not in st.session_state:
        st.session_state.challenge_start_time = None
    if 'coding_challenge_score' not in st.session_state:
        st.session_state.coding_challenge_score = 0
    if 'time_challenge_best' not in st.session_state:
        st.session_state.time_challenge_best = {}
    if 'username' not in st.session_state:
        st.session_state.username = "Player"
    if 'bookmarks' not in st.session_state:
        st.session_state.bookmarks = []
    if 'notes' not in st.session_state:
        st.session_state.notes = {}
    if 'study_time' not in st.session_state:
        st.session_state.study_time = 0
    if 'progress_data' not in st.session_state:
        st.session_state.progress_data = {}
    if 'completed_sections' not in st.session_state:
        st.session_state.completed_sections = set()

    
    # Apply theme toggle
    theme_toggle()

    # Add mobile responsive CSS
    mobile_responsive_css()
    
    # Sidebar navigation
    with st.sidebar:
        # Header with theme-aware color
        header_color = "#64b5f6" if st.session_state.get('dark_mode', False) else "#1e3c72"
        st.markdown(f"<h2 style='text-align: center; color: {header_color};'>🔗 Navigation</h2>", unsafe_allow_html=True)
        
        # Global Search with suggestions
        st.markdown("---")
        search_query = st.text_input("🔍 Search", placeholder="Search topics...", key="search_input")
        
        if search_query:
            query = search_query.strip()
            if len(query) > 0:
                # Show suggestions
                suggestions = get_search_suggestions(query)
                if suggestions:
                    st.write("**Suggestions:**")
                    for i, suggestion in enumerate(suggestions):
                        if st.button(f"💡 {suggestion}", key=f"suggest_{suggestion}_{i}"):
                            st.rerun()
                
                # Show results
                results = search_content(query)
                if results:
                    st.write("**Found in:**")
                    for i, result in enumerate(results):
                        completed = result in st.session_state.completed_sections
                        status = "✓" if completed else "○"
                        if st.button(f"{status} {result}", key=f"search_result_{result}_{i}"):
                            section_map = {'Introduction': 1, 'Types': 2, 'Operations': 3, 'Playground': 4, 'Analysis': 5, 'Practice': 6, 'Quiz': 8, 'Comparison': 9, 'Patterns': 14, 'Integration': 15}
                            if result in section_map:
                                st.session_state.current_tab = section_map[result]
                                st.rerun()
                else:
                    st.write("No results found")
        
        # Theme toggle
        st.markdown("---")
        theme_col1, theme_col2 = st.columns([1, 2])
        with theme_col1:
            theme_icon = "🌙" if not st.session_state.get('dark_mode', False) else "☀️"
            st.markdown(f"<div style='font-size: 1.5em; text-align: center;'>{theme_icon}</div>", unsafe_allow_html=True)
        with theme_col2:
            if st.button("Dark Mode" if not st.session_state.get('dark_mode', False) else "Light Mode", key="theme_toggle"):
                st.session_state.dark_mode = not st.session_state.get('dark_mode', False)
                st.rerun()
        
        st.markdown("---")
        
        # User stats display
        if st.session_state.user_score > 0:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {'#37474f' if st.session_state.get('dark_mode', False) else '#e3f2fd'} 0%, {'#455a64' if st.session_state.get('dark_mode', False) else '#bbdefb'} 100%); 
                        border-radius: 10px; padding: 10px; margin: 10px 0; text-align: center;">
                <div style="font-size: 0.9em; opacity: 0.8;">Your Score</div>
                <div style="font-size: 1.5em; font-weight: bold; color: {'#64b5f6' if st.session_state.get('dark_mode', False) else '#1e3c72'};">{st.session_state.user_score}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Navigation buttons
        nav_options = [
            ("🏠 Welcome", "Get started with linked lists"),
            ("📖 Introduction", "Learn the basics"),
            ("🔗 Types", "Explore different types"),
            ("⚙️ Operations", "Master operations & algorithms"),
            ("🎮 Playground", "Interactive practice"),
            ("📊 Analysis", "Performance comparison"),
            ("💡 Practice", "Solve problems"),
            ("🧪 Testing & Debugging", "Unit testing and debugging strategies"),
            ("📝 Interview Prep", "Top interview questions and tips"),
            ("🎨 Advanced Viz", "Advanced visualizations"),
            ("🧠 Quiz", "Test your knowledge"),
            ("⚖️ Comparison", "Compare data structures"),
            ("💾 Memory Mgmt", "Memory management topics"),
            ("🔒 Concurrency", "Thread-safe implementations"),
            ("🎆 Specialized", "Advanced linked list variants"),
            ("🚀 Optimizations", "Real-world implementation details"),
            ("🧩 Patterns", "Advanced problem patterns"),
            ("🔗 Integration", "Real-world integrations")
        ]
        
        for i, (name, desc) in enumerate(nav_options):
            # Highlight current tab
            button_type = "primary" if st.session_state.current_tab == i else "secondary"
            if st.button(name, key=f"nav_{i}", help=desc, use_container_width=True, type=button_type):
                st.session_state.current_tab = i
                st.session_state.scroll_to_top = True  # Flag to scroll to top
                st.rerun()
        
        st.markdown("---")
        
        # Progress indicator
        progress_pct = get_progress_percentage()
        st.markdown(f"""
        <div style="margin: 10px 0;">
            <div style="font-size: 0.9em; opacity: 0.8; text-align: center;">Progress: {progress_pct:.0f}%</div>
            <div style="background: {'#555' if st.session_state.get('dark_mode', False) else '#ddd'}; border-radius: 10px; height: 8px; margin: 5px 0;">
                <div style="background: {'#64b5f6' if st.session_state.get('dark_mode', False) else '#1e3c72'}; height: 8px; border-radius: 10px; width: {progress_pct}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bookmarks section
        if st.session_state.bookmarks:
            st.markdown("**📌 Bookmarks**")
            for bookmark in st.session_state.bookmarks[:3]:
                if st.button(f"📖 {bookmark}", key=f"bookmark_{bookmark}"):
                    section_map = {'Introduction': 1, 'Types': 2, 'Operations': 3, 'Playground': 4, 'Analysis': 5, 'Practice': 6, 'Quiz': 8, 'Comparison': 9, 'Patterns': 14, 'Integration': 15}
                    if bookmark in section_map:
                        st.session_state.current_tab = section_map[bookmark]
                        st.rerun()
        
        if st.session_state.get('achievements'):
            st.markdown(f"""
            <div style="text-align: center; margin: 10px 0;">
                <div style="font-size: 0.9em; opacity: 0.8;">Achievements</div>
                <div style="font-size: 1.2em;">🏆 {len(st.session_state.achievements)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        footer_color = "#b0b0b0" if st.session_state.get('dark_mode', False) else "#666"
        st.markdown(f"<p style='text-align: center; color: {footer_color}; font-size: 0.8em;'>Select a section above to explore</p>", unsafe_allow_html=True)

    # Add scroll to top functionality
    if st.session_state.get('scroll_to_top', False):
        # Force page to start from top by clearing and re-rendering
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("")
        st.session_state.scroll_to_top = False
    
    # Render the selected tab content
    if st.session_state.current_tab == 0:
        welcome_dashboard()
    elif st.session_state.current_tab == 1:
        introduction()
    elif st.session_state.current_tab == 2:
        types_of_linked_lists()
    elif st.session_state.current_tab == 3:
        operations_and_algorithms()
    elif st.session_state.current_tab == 4:
        interactive_playground()
    elif st.session_state.current_tab == 5:
        performance_analysis()
    elif st.session_state.current_tab == 6:
        practice_problems()
    elif st.session_state.current_tab == 7:
        testing_and_debugging()
    elif st.session_state.current_tab == 8:
        interview_preparation()
    elif st.session_state.current_tab == 9:
        advanced_visualizations()
    elif st.session_state.current_tab == 10:
        interactive_quiz()
    elif st.session_state.current_tab == 11:
        data_structure_comparison()
    elif st.session_state.current_tab == 12:
        memory_management()
    elif st.session_state.current_tab == 13:
        concurrent_linked_lists()
    elif st.session_state.current_tab == 14:
        specialized_linked_lists()
    elif st.session_state.current_tab == 15:
        real_world_optimizations()
    elif st.session_state.current_tab == 16:
        advanced_problem_patterns()
    elif st.session_state.current_tab == 17:
        integration_topics()
    
    # Close theme wrapper
    st.markdown('</div>', unsafe_allow_html=True)

# Run the main application
if __name__ == "__main__":
    main()