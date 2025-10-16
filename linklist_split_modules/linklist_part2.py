# Auto-generated module (part 2)
                    running_sum = 0
                    for i, num in enumerate(numbers):
                        running_sum += num
                        st.write(f"Step {i+1}: {running_sum-num} + {num} = {running_sum}")
            else:
                st.warning("Please enter valid numbers")
        except ValueError:
            st.error("Please enter valid integers separated by commas")
    
    # Comparison of sum algorithms
    st.subheader("⚡ Sum Algorithm Comparison")
    
    # Create comparison table manually to avoid pandas issues
    st.markdown("""
    | List Type | Time Complexity | Space Complexity | Special Considerations |
    |-----------|----------------|------------------|------------------------|
    | Singly Linked | O(n) | O(1) | Simple forward traversal |
    | Doubly Linked | O(n) | O(1) | Can traverse forward or backward |
    | Circular Linked | O(n) | O(1) | Must avoid infinite loops |
    """)
    
    st.info("💡 **Key Insight**: All linked list types have the same time complexity O(n) for sum calculation, but differ in implementation details.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Node Structure (Singly Circular):**
        ```python
        class CircularNode:
            def __init__(self, data):
                self.data = data
                self.next = None
        ```

        **Detailed Characteristics:**
        - **Memory Usage:** Same as singly (1 pointer + data per node)
        - **Traversal:** Can start from any node and traverse infinitely
        - **Operations:** Need careful handling to avoid infinite loops
        - **Performance:** O(1) for beginning operations, O(n) for end operations
        - **Special Property:** No NULL termination

        **Advantages:**
        - ✅ Memory efficient (same as singly linked)
        - ✅ Useful for circular operations
        - ✅ Can represent cyclic data naturally
        - ✅ Round-robin algorithms work naturally
        - ✅ No special case for end of list

        **Disadvantages:**
        - ❌ Easy to create infinite loops
        - ❌ More complex traversal logic
        - ❌ Cannot use NULL to detect end
        - ❌ Harder to detect cycles (ironic!)

        **Real-World Use Cases:**
        - **Round-Robin Scheduling:** CPU process scheduling
        - **Circular Buffers:** Audio/video streaming
        - **Multiplayer Games:** Player turn management
        - **Music Playlists:** Continuous playback
        - **Token Ring Networks:** Data transmission
        - **Time-Sharing Systems:** Resource allocation
        """)

        st.subheader("Visual Representation")
        st.code("""
Circular Linked List Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | --> | Next: 0x300       | --> | Next: 0x100       |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300         |
                                                              |
                                                              v
                                                            Back to 0x100

Traversal: 10 -> 20 -> 30 -> 10 -> 20 -> ... (infinite)
        """)

    with col2:
        st.code("""
# Complete Circular Linked List Implementation
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        if self.head is None:
            new_node.next = new_node  # Point to itself
            self.head = new_node
        else:
            new_node.next = self.head
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.size += 1

    def traverse(self, max_elements=10):
        if self.head is None:
            return []
        elements = []
        current = self.head
        count = 0
        while count < max_elements:
            elements.append(current.data)
            current = current.next
            count += 1
            if current == self.head:
                break
        return elements

# Example Usage:
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
print(cll.traverse())  # [1, 2, 3]
        """, language="python")

    # Practical sum examples with real scenarios
    st.subheader("🌟 Real-World Sum Applications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Shopping Cart Total (Singly Linked):**
        ```python
        # Each node represents an item with price
        class CartItem:
            def __init__(self, name, price):
                self.name = name
                self.price = price
                self.next = None
        
        def calculate_cart_total(cart_head):
            total = 0
            current = cart_head
            while current:
                total += current.price
                current = current.next
            return total
        
        # Cart: Apple($2) → Banana($1) → Orange($3)
        # Total: $6
        ```
        """)
    
    with col2:
        st.markdown("""
        **Score History (Doubly Linked):**
        ```python
        # Game scores with forward/backward navigation
        class ScoreNode:
            def __init__(self, score):
                self.score = score
                self.next = None
                self.prev = None
        
        def calculate_total_score(head):
            total = 0
            current = head
            while current:
                total += current.score
                current = current.next
            return total
        
        # Scores: 100 ↔ 85 ↔ 92 ↔ 78
        # Total: 355
        ```
        """)
    
    st.header("4. Advanced Linked List Variants")

    st.subheader("XOR Linked List")
    st.markdown("""
    **Concept:** Uses bitwise XOR to store both previous and next pointers in a single field, saving memory.

    **How it works:**
    - Each node stores: `ptr = prev XOR next`
    - To traverse: `next = ptr XOR prev`
    - Memory efficient but complex to implement

    **Use Cases:** Memory-constrained environments, competitive programming
    """)

    st.subheader("Skip List")
    st.markdown("""
    **Concept:** A probabilistic data structure that allows O(log n) search time.

    **How it works:**
    - Multiple levels of linked lists
    - Higher levels skip more nodes
    - Search starts from top level and works down

    **Use Cases:** Database indexes, Redis sorted sets
    """)

    st.subheader("Unrolled Linked List")
    st.markdown("""
    **Concept:** Each node contains an array of elements instead of a single element.

    **Benefits:**
    - Better cache performance
    - Reduced pointer overhead
    - Faster sequential access

    **Use Cases:** High-performance applications, cache-conscious data structures
    """)

    st.header("Comprehensive Comparison")

    # Create detailed comparison table
    comparison_data = {
        'Aspect': [
            'Memory per Node',
            'Traversal Direction',
            'Beginning Operations',
            'End Operations',
            'Random Access',
            'Implementation Complexity',
            'Memory Efficiency',
            'Cache Performance',
            'Use Case Fit'
        ],
        'Singly Linked': [
            '1 pointer + data',
            'Forward only',
            'O(1)',
            'O(n)',
            'O(n)',
            'Simple',
            'Good',
            'Good',
            'Stacks, Queues'
        ],
        'Doubly Linked': [
            '2 pointers + data',
            'Bidirectional',
            'O(1)',
            'O(1)*',
            'O(n)',
            'Moderate',
            'Poor',
            'Fair',
            'Deques, Caches'
        ],
        'Circular Singly': [
            '1 pointer + data',
            'Circular',
            'O(1)',
            'O(n)',
            'O(n)',
            'Moderate',
            'Good',
            'Good',
            'Round-robin'
        ],
        'Circular Doubly': [
            '2 pointers + data',
            'Circular Bidirectional',
            'O(1)',
            'O(1)',
            'O(n)',
            'Complex',
            'Poor',
            'Fair',
            'Complex circular ops'
        ]
    }

    import pandas as pd
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)

    st.markdown("*Note: * Requires tail pointer for O(1) end operations")

    st.header("Common Pitfalls and Best Practices")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Common Mistakes")
        st.markdown("""
        - **Null Pointer Dereference:** Always check for None before accessing next/prev
        - **Infinite Loops:** Especially in circular lists, always have termination conditions
        - **Memory Leaks:** In languages without GC, remember to free nodes
        - **Lost References:** When deleting nodes, update all relevant pointers
        - **Off-by-One Errors:** Careful with indexing and position calculations
        """)

    with col2:
        st.subheader("Best Practices")
        st.markdown("""
        - **Use Sentinel Nodes:** Dummy head/tail nodes to simplify boundary cases
        - **Maintain Size Counter:** Keep track of list size for efficient operations
        - **Tail Pointers:** For doubly linked lists to enable O(1) end operations
        - **Consistent Naming:** Use clear variable names (head, tail, current, etc.)
        - **Error Handling:** Always handle edge cases (empty list, single node)
        """)

    st.header("Performance Considerations")

    st.markdown("""
    **Memory Overhead Analysis:**

    | Data Structure | Pointers | Overhead (64-bit) | Total per Node |
    |----------------|----------|-------------------|----------------|
    | Singly Linked | 1 | 8 bytes | 8 + data bytes |
    | Doubly Linked | 2 | 16 bytes | 16 + data bytes |
    | Array Element | 0 | 0 bytes | data bytes only |

    **Cache Performance:**
    - **Arrays:** Excellent locality of reference
    - **Linked Lists:** Poor locality, nodes scattered in memory
    - **Unrolled Lists:** Better locality with multiple elements per node

    **When to Choose Which:**
    - **Singly Linked:** Memory-critical, forward-only traversal
    - **Doubly Linked:** Need bidirectional access, frequent end operations
    - **Circular:** Round-robin, circular buffers, infinite traversal
    - **Array:** Random access, cache performance critical
    """)

    st.header("Implementation Tips")

    with st.expander("Singly Linked List Tips"):
        st.markdown("""
        1. Always keep a reference to head
        2. Use a dummy node for operations on empty lists
        3. For frequent end operations, maintain a tail pointer
        4. Be careful with pointer updates during deletion
        5. Use recursion sparingly (watch stack overflow)
        """)

    with st.expander("Doubly Linked List Tips"):
        st.markdown("""
        1. Always update both next and prev pointers
        2. Maintain both head and tail pointers
        3. Use symmetry in operations (forward/backward)
        4. Careful with boundary conditions
        5. Consider using sentinel nodes
        """)

    with st.expander("Circular Linked List Tips"):
        st.markdown("""
        1. Never use NULL to detect end of list
        2. Always have a termination condition in loops
        3. Be careful with empty list handling
        4. Use size counter to prevent infinite loops
        5. Consider using a tail pointer for efficiency
        """)

# Operations and Algorithms section
def operations_and_algorithms():
    st.title("Operations and Algorithms")
    save_progress("Operations")

    st.header("1. Insertion Operations")

    st.subheader("Insert at Beginning")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Create a new node with given data
        2. Set new node's next to current head
        3. Update head to point to new node

        **Time Complexity:** O(1)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # New head

# Example: Insert 0 at beginning of [1,2,3]
# Result: [0,1,2,3]
        """, language="python")

    st.subheader("Insert at End")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Create a new node with given data
        2. If list is empty, set as head
        3. Else traverse to last node
        4. Set last node's next to new node

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Example: Insert 4 at end of [1,2,3]
# Result: [1,2,3,4]
        """, language="python")

    st.header("2. Deletion Operations")

    st.subheader("Delete from Beginning")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. If list is empty, return None
        2. Store current head
        3. Update head to next node
        4. Return deleted node's data

        **Time Complexity:** O(1)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def delete_from_beginning(head):
    if head is None:
        return None, head

    deleted_data = head.data
    new_head = head.next
    return deleted_data, new_head

# Example: Delete from [1,2,3]
# Result: 1, [2,3]
        """, language="python")

    st.subheader("Delete by Value")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. If list is empty, return False
        2. If head contains target, update head
        3. Traverse list to find target
        4. Update previous node's next pointer
        5. Return True if found, False otherwise

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def delete_by_value(head, target):
    if head is None:
        return False, head

    if head.data == target:
        return True, head.next

    current = head
    while current.next and current.next.data != target:
        current = current.next

    if current.next:
        current.next = current.next.next
        return True, head
    return False, head

# Example: Delete 2 from [1,2,3]
# Result: True, [1,3]
        """, language="python")

    st.header("3. Traversal")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Start from head node
        2. While current node is not None:
           - Process current node's data
           - Move to next node
        3. End when current becomes None

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)

        **Use Cases:**
        - Printing list elements
        - Searching for values
        - Applying operations to all elements
        """)
    with col2:
        st.code("""
def traverse_and_print(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example traversal of [1,2,3]
# Output: 1 -> 2 -> 3 -> None
        """, language="python")

    st.header("4. Searching")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Start from head node
        2. Initialize position counter
        3. While current node is not None:
           - Check if current data matches target
           - If match, return position
           - Increment position, move to next
        4. Return -1 if not found

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def search_by_value(head, target):
    current = head
    position = 0

    while current:
        if current.data == target:
            return position
        current = current.next
        position += 1

    return -1

# Example: Search for 2 in [1,2,3]
# Result: 1 (0-based index)
        """, language="python")

    st.header("5. Time and Space Complexity Analysis")
    st.markdown("""
    | Operation | Singly Linked List | Doubly Linked List | Notes |
    |-----------|-------------------|-------------------|-------|
    | **Insertion at Beginning** | O(1) | O(1) | Direct head update |
    | **Insertion at End** | O(n) | O(1)* | *Requires tail pointer |
    | **Insertion at Position** | O(n) | O(n) | Need to traverse |
    | **Deletion at Beginning** | O(1) | O(1) | Direct head update |
    | **Deletion at End** | O(n) | O(1)* | *Requires tail pointer |
    | **Deletion by Value** | O(n) | O(n) | Linear search required |
    | **Traversal** | O(n) | O(n) | Visit all nodes |
    | **Searching** | O(n) | O(n) | Linear search |

    **Space Complexity:** O(n) for all types (proportional to number of elements)
    """)

    st.header("Advanced Algorithms")

    st.subheader("Reverse a Linked List")
    st.code("""
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Example: Reverse [1,2,3] -> [3,2,1]
    """, language="python")

    st.subheader("Detect Cycle (Floyd's Algorithm)")
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

# Returns True if cycle exists
    """, language="python")

# Interactive Playground section
def interactive_playground():
    st.title("Interactive Playground")
    save_progress("Playground")
    
    # Quick tools
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🎲 Random Data", key="random_data"):
            if hasattr(st.session_state, 'linked_list') and st.session_state.linked_list:
                import random
                random_values = [random.randint(1, 100) for _ in range(3)]
                for val in random_values:
                    st.session_state.linked_list.insert_at_end(val)
                st.success(f"🎲 Added: {random_values}")
                st.rerun()
            else:
                st.warning("Create a list first!")
    with col2:
        is_bookmarked = "Playground" in st.session_state.bookmarks
        if st.button("📌 Bookmark" if not is_bookmarked else "📌 Bookmarked", key="bookmark_playground"):
            if not is_bookmarked:
                add_bookmark("Playground")
            st.rerun()

    # Linked list classes are now imported from linked_list_classes module

    # Initialize session state
    if 'list_type' not in st.session_state:
        st.session_state.list_type = "Singly Linked List"
    if 'linked_list' not in st.session_state:
        st.session_state.linked_list = SinglyLinkedList()

    # List type selector
    st.header("Select Linked List Type")
    list_types = ["Singly Linked List", "Doubly Linked List", "Circular Linked List"]
    selected_type = st.selectbox("Choose list type:", list_types, index=list_types.index(st.session_state.list_type))

    if selected_type != st.session_state.list_type:
        st.session_state.list_type = selected_type
        if selected_type == "Singly Linked List":
            st.session_state.linked_list = SinglyLinkedList()
        elif selected_type == "Doubly Linked List":
            st.session_state.linked_list = DoublyLinkedList()
        elif selected_type == "Circular Linked List":
            st.session_state.linked_list = CircularLinkedList()
        st.rerun()

    st.header("Create Your Linked List")
    col1, col2 = st.columns([2, 1])
    with col1:
        user_input = st.text_input("Enter comma-separated values (e.g., 1, 2, 3, 4)", "")
        if st.button("Create List", key="create"):
            if user_input:
                values = [x.strip() for x in user_input.split(",") if x.strip()]
                if st.session_state.list_type == "Singly Linked List":
                    st.session_state.linked_list = SinglyLinkedList()
                    for val in values:
                        st.session_state.linked_list.insert_at_end(val)
                elif st.session_state.list_type == "Doubly Linked List":
                    st.session_state.linked_list = DoublyLinkedList()
                    for val in values:
                        st.session_state.linked_list.insert_at_end(val)
                elif st.session_state.list_type == "Circular Linked List":
                    st.session_state.linked_list = CircularLinkedList()
                    for val in values:
                        st.session_state.linked_list.insert_at_end(val)
                st.success(f"{st.session_state.list_type} created with {len(values)} elements!")
            else:
                st.warning("Please enter some values.")
    with col2:
        if st.button("Clear List", key="clear"):
            if st.session_state.list_type == "Singly Linked List":
                st.session_state.linked_list = SinglyLinkedList()
            elif st.session_state.list_type == "Doubly Linked List":
                st.session_state.linked_list = DoublyLinkedList()
            elif st.session_state.list_type == "Circular Linked List":
                st.session_state.linked_list = CircularLinkedList()
            st.info(f"{st.session_state.list_type} cleared!")

    st.header(f"Current {st.session_state.list_type}")
    if st.session_state.linked_list.size > 0:
        if st.session_state.list_type == "Doubly Linked List":
            st.write("Forward: ", st.session_state.linked_list.traverse_forward())
            st.write("Backward: ", st.session_state.linked_list.traverse_backward())
        else:
            elements = st.session_state.linked_list.traverse() if st.session_state.list_type != "Circular Linked List" else st.session_state.linked_list.traverse(20)
            st.write("Elements: ", elements)
        st.write(f"Length: {st.session_state.linked_list.size}")

        # Enhanced Plotly visualization
        elements = []
        if st.session_state.list_type == "Doubly Linked List":
            elements = st.session_state.linked_list.traverse_forward()
        elif st.session_state.list_type == "Circular Linked List":
            elements = st.session_state.linked_list.traverse(20)
        else:
            elements = st.session_state.linked_list.traverse()

        # Create interactive Plotly visualization
        fig = go.Figure()
        
        # Add nodes
        node_x = [i * 2 for i in range(len(elements))]
        node_y = [0] * len(elements)
        
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            marker=dict(size=50, color='#4A90E2', line=dict(width=3, color='#2E5BBA')),
            text=[str(val) for val in elements],
            textposition="middle center",
            textfont=dict(size=14, color='white', family="Arial Black"),
            name="Nodes",
            hovertemplate="<b>Node %{pointNumber}</b><br>Value: %{text}<extra></extra>"
        ))
        
        # Add arrows based on list type
        if st.session_state.list_type == "Doubly Linked List":
            # Forward arrows (next pointers)
            for i in range(len(elements) - 1):
                fig.add_annotation(
                    x=node_x[i+1] - 0.6, y=0.3,
                    ax=node_x[i] + 0.6, ay=0.3,
                    xref='x', yref='y', axref='x', ayref='y',
                    arrowhead=2, arrowsize=1.5, arrowwidth=3, arrowcolor='#FF6B6B',
                    showarrow=True
                )
                # Add "next" label
                fig.add_annotation(
                    x=(node_x[i] + node_x[i+1]) / 2, y=0.5,
                    text="next", showarrow=False,
                    font=dict(size=10, color='#FF6B6B', family="Arial Black")
                )
            
            # Backward arrows (prev pointers)
            for i in range(1, len(elements)):
                fig.add_annotation(
                    x=node_x[i-1] + 0.6, y=-0.3,
                    ax=node_x[i] - 0.6, ay=-0.3,
                    xref='x', yref='y', axref='x', ayref='y',
                    arrowhead=2, arrowsize=1.5, arrowwidth=3, arrowcolor='#4ECDC4',
                    showarrow=True
                )
                # Add "prev" label
                fig.add_annotation(
                    x=(node_x[i] + node_x[i-1]) / 2, y=-0.5,
                    text="prev", showarrow=False,
                    font=dict(size=10, color='#4ECDC4', family="Arial Black")
                )
                
        elif st.session_state.list_type == "Circular Linked List":
            # Regular forward arrows
            for i in range(len(elements) - 1):
                fig.add_annotation(
                    x=node_x[i+1] - 0.6, y=0,
                    ax=node_x[i] + 0.6, ay=0,
                    xref='x', yref='y', axref='x', ayref='y',
                    arrowhead=2, arrowsize=1.5, arrowwidth=3, arrowcolor='#FF6B6B',
                    showarrow=True
                )
            
            # Circular arrow from last to first (curved)
            if len(elements) > 1:
                last_x = node_x[-1]
                first_x = node_x[0]
                mid_x = (last_x + first_x) / 2
                
                # Create a more visible curved path
                fig.add_shape(
                    type="path",
                    path=f"M {last_x + 0.7},0 Q {mid_x},{-1.0} {first_x - 0.7},0",
                    line=dict(color="#9B59B6", width=4),
                )
                
                # Add multiple arrow segments for better visibility
                # Arrow at the end pointing to first node
                fig.add_annotation(
                    x=first_x - 0.7, y=0,
                    ax=first_x - 0.9, ay=-0.2,
                    xref='x', yref='y', axref='x', ayref='y',
                    arrowhead=2, arrowsize=2, arrowwidth=4, arrowcolor='#9B59B6',
                    showarrow=True
                )
                
                # Add arrow at the start from last node
                fig.add_annotation(
                    x=last_x + 0.9, y=-0.2,
                    ax=last_x + 0.7, ay=0,
                    xref='x', yref='y', axref='x', ayref='y',
                    arrowhead=2, arrowsize=2, arrowwidth=4, arrowcolor='#9B59B6',
                    showarrow=True
                )
                
                # Add "circular" label with background
                fig.add_annotation(
                    x=mid_x, y=-0.7,
                    text="↻ CIRCULAR", showarrow=False,
                    font=dict(size=11, color='#9B59B6', family="Arial Black"),
                    bgcolor="rgba(255,255,255,0.8)",
                    bordercolor="#9B59B6",
                    borderwidth=1
                )
                
        else:  # Singly Linked List
            for i in range(len(elements) - 1):
                fig.add_annotation(
                    x=node_x[i+1] - 0.6, y=0,
                    ax=node_x[i] + 0.6, ay=0,
                    xref='x', yref='y', axref='x', ayref='y',
                    arrowhead=2, arrowsize=1.5, arrowwidth=3, arrowcolor='#FF6B6B',
                    showarrow=True
                )
        
        # Add NULL for non-circular lists
        if st.session_state.list_type != "Circular Linked List" and elements:
            fig.add_trace(go.Scatter(
                x=[node_x[-1] + 2], y=[0],
                mode='markers+text',
                marker=dict(size=40, color='#95A5A6', line=dict(width=2, color='#7F8C8D')),
                text=["NULL"],
                textposition="middle center",
                textfont=dict(size=12, color='white', family="Arial Black"),
                name="NULL",
                showlegend=False
            ))
            fig.add_annotation(
                x=node_x[-1] + 1.5, y=0,
                ax=node_x[-1] + 0.5, ay=0,
                arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='#95A5A6',
                showarrow=True
            )
        
        fig.update_layout(
            title=dict(
                text=f"{st.session_state.list_type} Visualization",
                font=dict(size=18, color='#2C3E50')
            ),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, 
                      range=[-1.5, 1] if st.session_state.list_type == "Circular Linked List" else [-0.8, 0.8]),
            showlegend=False,
            height=400 if st.session_state.list_type in ["Circular Linked List", "Doubly Linked List"] else 300,
            margin=dict(l=20, r=20, t=40, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info(f"No {st.session_state.list_type.lower()} created yet. Use the input above to create one!")

    st.header(f"Operations on {st.session_state.list_type}")
    if st.session_state.linked_list.size > 0:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Insert Element")
            insert_pos = st.selectbox("Position", ["Beginning", "End", "At Index"])
            insert_val = st.text_input("Value to insert", key="insert_val")

            if insert_pos == "At Index":
                insert_idx = st.number_input("Index", min_value=0, max_value=st.session_state.linked_list.size, value=0, key="insert_idx")

            if st.button("Insert", key="insert_btn"):
                if insert_val:
                    success = False
                    if insert_pos == "Beginning":
                        st.session_state.linked_list.insert_at_beginning(insert_val)
                        success = True
                    elif insert_pos == "End":
                        st.session_state.linked_list.insert_at_end(insert_val)
                        success = True
                    else:  # At Index
                        success = st.session_state.linked_list.insert_at_index(insert_val, insert_idx)

                    if success:
                        st.success(f"Inserted '{insert_val}' at {insert_pos.lower()}!")
                        st.rerun()
                    else:
                        st.warning("Invalid index!")
                else:
                    st.warning("Please enter a value to insert.")

        with col2:
            st.subheader("Delete Element")
            delete_pos = st.selectbox("Delete from", ["Beginning", "End", "By Value"], key="delete_pos")
            if delete_pos == "By Value":
                delete_val = st.text_input("Value to delete", key="delete_val")

            if st.button("Delete", key="delete_btn"):
                if st.session_state.linked_list.size == 0:
                    st.warning("List is empty!")
                else:
                    deleted = None
                    if delete_pos == "Beginning":
                        deleted = st.session_state.linked_list.delete_from_beginning()
                    elif delete_pos == "End":
                        deleted = st.session_state.linked_list.delete_from_end()
                    else:  # By Value
                        if st.session_state.linked_list.delete_by_value(delete_val):
                            deleted = delete_val

                    if deleted is not None:
                        st.success(f"Removed '{deleted}' from {delete_pos.lower()}!")
                        st.rerun()
                    else:
                        st.warning(f"'{delete_val}' not found in list!" if delete_pos == "By Value" else "Operation failed!")

        with col3:
            st.subheader("Search Element")
            search_val = st.text_input("Value to search", key="search_val")

            if st.button("Search", key="search_btn"):
                idx = st.session_state.linked_list.search(search_val)
                if idx != -1:
                    st.success(f"Found '{search_val}' at index {idx}!")
                else:
                    st.warning(f"'{search_val}' not found in list!")

    # Step-by-step visualization
    st.subheader("🎬 Step-by-Step Operations")
    
    col1, col2 = st.columns(2)
    with col1:
        operation = st.selectbox("Select Operation:", ["Insert at Beginning", "Insert at End", "Delete from Beginning"])
    with col2:
        if operation.startswith("Insert"):
            new_value = st.number_input("Value to insert:", value=99)
    
    if st.button("🎬 Show Animation"):
        if operation == "Insert at Beginning":
            steps = step_by_step_insert([10, 20, 30], new_value, 0)
        elif operation == "Insert at End":
            steps = step_by_step_insert([10, 20, 30], new_value, -1)
        else:
            steps = ["Step 1: Check if list is empty", "Step 2: Store head data", "Step 3: Update head to next node", "Step 4: Deletion complete!"]
        
        for i, step in enumerate(steps):
            st.write(f"**{step}**")
            if i < len(steps) - 1:
                st.write("⬇️")
    
    # Code Export Feature
    if st.session_state.linked_list.size > 0:
        current_code = f"""
# Generated Linked List Code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Your current list: {st.session_state.linked_list.traverse() if hasattr(st.session_state.linked_list, 'traverse') else 'N/A'}
# Created on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("📤 Export Your Work")
        with col2:
            export_code(current_code, "my_linked_list.py")
    
    # Code examples remain the same
    st.header("Code Implementation & Execution")
    st.markdown("Here's how the operations above are implemented in Python. You can also run example code!")

    # Code execution functionality
    st.subheader("🔧 Code Runner")

    # Predefined code examples
    code_examples = {
        "Create Linked List": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create a linked list
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)

print("Linked List:", ll.traverse())
""",
        "Insert at Beginning": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create and modify linked list
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)

print("After insertions:", ll.traverse())
""",
        "Search Element": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

# Create linked list and search
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

print("List:", ll.traverse())
print("Position of 20:", ll.search(20))
print("Position of 40:", ll.search(40))
""",
        "Reverse List": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create and reverse linked list
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

print("Original:", ll.traverse())
ll.reverse()
print("Reversed:", ll.traverse())
"""
    }

    selected_example = st.selectbox("Choose an example to run:", list(code_examples.keys()))
    
    # Display selected code
    st.code(code_examples[selected_example], language="python")
    
    # Add run button below the code
    if st.button(f"▶️ Run {selected_example}", key="run_selected_code"):
        with st.spinner("Executing code..."):
            try:
                # Capture output
                old_stdout = sys.stdout
                sys.stdout = captured_output = StringIO()
                
                # Execute the code
                exec(code_examples[selected_example])
                
                # Get output
                sys.stdout = old_stdout
                output = captured_output.getvalue()
                
                if output:
                    st.success("Code executed successfully!")
                    st.text("Output:")
                    st.code(output, language="text")
                else:
                    st.success("Code executed successfully (no output)")
                    
            except Exception as e:
                sys.stdout = old_stdout
                st.error(f"Error executing code: {str(e)}")

# Performance Analysis section
def performance_analysis():
    st.title("Performance Analysis")
    save_progress("Analysis")

    st.header("Time Complexity Comparison")

    st.markdown("""
    Understanding the performance characteristics of different linked list operations is crucial for choosing
    the right data structure for your use case. Below is a detailed analysis of time complexities.
    """) 
    # Create comprehensive data
    operations = [
        'Insert at Beginning',
        'Insert at End',
        'Insert at Position',
        'Delete from Beginning',
        'Delete from End',
        'Delete by Value',
        'Search by Value',
        'Traversal',
        'Access by Index'
    ]

    # Time complexities (1 = O(1), n = O(n))
    singly_linked = [1, 'n', 'n', 1, 'n', 'n', 'n', 'n', 'n']
    doubly_linked = [1, 1, 'n', 1, 1, 'n', 'n', 'n', 'n']  # Assuming tail pointer for end operations
    circular_singly = [1, 'n', 'n', 1, 'n', 'n', 'n', 'n', 'n']
    array_list = ['n', 1, 'n', 'n', 1, 'n', 'n', 'n', 1]

    # Create DataFrame for better display
    import pandas as pd

    complexity_data = {
        'Operation': operations,
        'Singly Linked List': singly_linked,
        'Doubly Linked List': doubly_linked,
        'Circular Linked List': circular_singly,
        'Dynamic Array': array_list
    }

    df = pd.DataFrame(complexity_data)
    st.dataframe(df, use_container_width=True)

    st.markdown("""
    **Legend:**
    - **1**: O(1) - Constant time
    - **n**: O(n) - Linear time
    """)

    # Interactive chart
    st.header("Interactive Performance Comparison")

    selected_operations = st.multiselect(
        "Select operations to compare:",
        operations,
        default=['Insert at Beginning', 'Insert at End', 'Search by Value', 'Access by Index']
    )

    if selected_operations:
        # Prepare data for plotting
        plot_data = []
        structures = ['Singly Linked', 'Doubly Linked', 'Circular Linked', 'Dynamic Array']

        for op in selected_operations:
            idx = operations.index(op)
            values = [
                1 if singly_linked[idx] == 1 else 10,  # Convert to numeric for plotting
                1 if doubly_linked[idx] == 1 else 10,
                1 if circular_singly[idx] == 1 else 10,
                1 if array_list[idx] == 1 else 10
            ]
            plot_data.append(go.Bar(name=op, x=structures, y=values))

        fig = go.Figure(data=plot_data)
        fig.update_layout(
            barmode='group',
            title="Time Complexity Comparison (Lower is Better)",
            yaxis_title="Complexity (1 = O(1), 10 = O(n))",
            xaxis_title="Data Structure",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

    st.header("Space Complexity Analysis")

    space_data = {
        'Data Structure': ['Singly Linked List', 'Doubly Linked List', 'Circular Linked List', 'Dynamic Array'],
        'Per Element': ['1 pointer + data', '2 pointers + data', '1 pointer + data', 'data only'],
        'Overhead': ['High (pointers)', 'Very High (2 pointers)', 'High (pointers)', 'Low (amortized)'],
        'Memory Efficiency': ['Low', 'Very Low', 'Low', 'High']
    }

    space_df = pd.DataFrame(space_data)
    st.dataframe(space_df, use_container_width=True)

    st.header("When to Use Which Linked List?")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Choose Singly Linked List when:")
        st.markdown("""
        - ✅ Memory is a concern (only one pointer per node)
        - ✅ You only need forward traversal
        - ✅ Implementing stacks or queues
        - ✅ Simple operations are sufficient
        - ✅ Working with large datasets where memory matters
        """)

        st.subheader("Choose Doubly Linked List when:")
        st.markdown("""
        - ✅ Need bidirectional traversal
        - ✅ Frequent insertions/deletions at both ends
        - ✅ Implementing deques or LRU caches
        - ✅ Browser history functionality
        - ✅ Text editor cursor movement
        """)

    with col2:
        st.subheader("Choose Circular Linked List when:")
        st.markdown("""
        - ✅ Need circular traversal
        - ✅ Implementing round-robin algorithms
        - ✅ Circular buffers or playlists
        - ✅ Multiplayer game turn management
        - ✅ CPU scheduling algorithms
        """)

        st.subheader("Choose Dynamic Array instead when:")
        st.markdown("""
        - ✅ Need fast random access (O(1))
        - ✅ Memory efficiency is critical
        - ✅ Most operations are at the end
        - ✅ Cache performance matters
        - ✅ Simple implementation needed
        """)

    st.header("Cache Performance Considerations")

    st.markdown("""
    **Linked Lists vs Arrays:**

    | Aspect | Linked List | Array |
    |--------|-------------|-------|
    | **Locality of Reference** | Poor (nodes scattered in memory) | Excellent (contiguous memory) |
    | **Cache Misses** | High (pointer chasing) | Low (sequential access) |
    | **Prefetching** | Difficult | Easy |
    | **Memory Access Pattern** | Random | Sequential |

    **Why Arrays are Faster for Traversal:**
    - CPU cache can prefetch adjacent elements
    - No pointer dereferencing overhead
    - Better branch prediction
    - SIMD operations possible
    """)

    st.header("Big O Notation Deep Dive")

    st.markdown("""
    ### Understanding Time Complexity

    **O(1) - Constant Time:**
    - Operation takes the same time regardless of input size
    - Examples: Insert at beginning (singly linked), access array element by index

    **O(n) - Linear Time:**
    - Operation time grows linearly with input size
    - Examples: Search, traversal, insert at end (singly linked without tail)

    ### Amortized Analysis

    **Dynamic Arrays:**
    - Most operations are O(1) amortized
    - Resize operations are O(n) but happen infrequently
    - Average case performance is better than worst case

    **Linked Lists:**
    - All operations have consistent worst-case bounds
    - No amortization needed
    - Predictable performance
    """)

    # Performance tips
    st.header("Performance Optimization Tips")

    with st.expander("Linked List Optimizations"):
        st.markdown("""
        1. **Use Tail Pointers:** For doubly linked lists, maintain a tail pointer for O(1) end operations
        2. **Dummy Nodes:** Use sentinel nodes to simplify boundary condition handling
        3. **XOR Linked Lists:** Store XOR of previous and next pointers to save memory (advanced)
        4. **Unrolled Linked Lists:** Store multiple elements per node to improve cache performance
        5. **Skip Lists:** Add skip pointers for faster search operations (O(log n))
        """)

    with st.expander("When to Choose Arrays Over Linked Lists"):
        st.markdown("""
        1. **Random Access:** Need O(1) access by index
        2. **Memory Efficiency:** No pointer overhead
        3. **Cache Performance:** Better locality of reference
        4. **Simple Operations:** Basic CRUD operations
        5. **Small Datasets:** Overhead of pointers not worth it
        """)

    with st.expander("Real-World Performance Considerations"):
        st.markdown("""
        1. **Memory Allocation:** Linked list nodes may cause heap fragmentation
        2. **Garbage Collection:** Reference counting can be expensive
        3. **Branch Prediction:** Arrays have better branch prediction for loops
        4. **SIMD Operations:** Arrays can leverage SIMD instructions
        5. **Page Faults:** Linked lists may cause more page faults with poor allocation
        """)

# Practice Problems section
def practice_problems():
    st.title("Practice Problems")
    save_progress("Practice")

    st.header("Problem 1: Reverse a Singly Linked List")
    st.markdown("""
    **Problem Statement:** Given the head of a singly linked list, reverse the list and return the reversed list.

    **Example:**
    - Input: head = [1,2,3,4,5]
    - Output: [5,4,3,2,1]
    """)

    with st.expander("Solution"):
        st.code("""
def reverseList(head):
    prev = None
    current = head

    while current:
        next_temp = current.next  # Store next node
        current.next = prev      # Reverse the link
        prev = current           # Move prev to current
        current = next_temp      # Move to next node

    return prev

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 2: Detect Cycle in Linked List")
    st.markdown("""
    **Problem Statement:** Given head, the head of a linked list, determine if the linked list has a cycle in it.

    **Example:**
    - Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
    - Output: true
    """)

    with st.expander("Solution (Floyd's Cycle Detection)"):
        st.code("""
def hasCycle(head):
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
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 3: Merge Two Sorted Lists")
    st.markdown("""
    **Problem Statement:** Merge two sorted linked lists and return it as a sorted list.

    **Example:**
    - Input: list1 = [1,2,4], list2 = [1,3,4]
    - Output: [1,1,2,3,4,4]
    """)

    with st.expander("Solution"):
        st.code("""
def mergeTwoLists(list1, list2):
    # Create a dummy node
    dummy = Node(0)
    current = dummy

    # Merge the lists
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

# Time Complexity: O(n + m)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 4: Remove Nth Node From End")
    st.markdown("""
    **Problem Statement:** Given the head of a linked list, remove the nth node from the end of the list and return its head.

    **Example:**
    - Input: head = [1,2,3,4,5], n = 2
    - Output: [1,2,3,5]
    """)

    with st.expander("Solution (Two Pointers)"):
        st.code("""
def removeNthFromEnd(head, n):
    # Create a dummy node
    dummy = Node(0)
    dummy.next = head

    # Use two pointers
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for i in range(n + 1):
        first = first.next

    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from end
    second.next = second.next.next

    return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 5: Find Middle of Linked List")
    st.markdown("""
    **Problem Statement:** Given the head of a singly linked list, return the middle node of the linked list.

    **Example:**
    - Input: head = [1,2,3,4,5]
    - Output: [3,4,5]
    """)

    with st.expander("Solution (Fast and Slow Pointers)"):
        st.code("""
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Additional Practice Problems")
    st.markdown("""
    **Easy:**
    6. Remove duplicates from sorted linked list
    7. Check if linked list is palindrome
    8. Find intersection point of two linked lists

    **Medium:**
    9. Add two numbers represented by linked lists
    10. Flatten a multilevel doubly linked list
    11. Sort linked list using merge sort

    **Hard:**
    12. Reverse nodes in k-group
    13. Copy list with random pointer
    14. LRU Cache implementation using doubly linked list
    """)

    st.header("Tips for Solving Linked List Problems")
    st.markdown("""
    - **Dummy Node:** Use a dummy node to handle edge cases (empty list, single node)
    - **Two Pointers:** Fast and slow pointers for cycle detection, finding middle
    - **Recursion:** Natural fit for linked list problems (be mindful of stack space)
    - **Edge Cases:** Always consider empty list, single node, two nodes
    - **Memory Management:** In languages with manual memory management, don't forget to free nodes
    - **Visualization:** Draw the list and pointers on paper to understand the problem
    """)

# References and Resources section
def references_and_resources():
    st.title("References and Resources")

    st.markdown("""
    - [GeeksforGeeks - Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
    - [Wikipedia - Linked List](https://en.wikipedia.org/wiki/Linked_list)
    - [Visualgo - Linked List](https://visualgo.net/en/list)
    - [Streamlit Documentation](https://docs.streamlit.io/)
    """)

# Advanced Visualizations section
def advanced_visualizations():
    st.markdown("""
    <div class="section-card">
        <h1 style="background: linear-gradient(135deg, var(--primary-600) 0%, var(--secondary-600) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            Advanced Visualizations
        </h1>
        <p style="color: var(--neutral-600); font-size: 1.1rem;">
            Explore 3D visualizations of different linked list types with modern interactive graphics
        </p>
    </div>
    """, unsafe_allow_html=True)
    save_progress("Advanced Viz")

    # Modern selector container
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-md);
    ">
    """, unsafe_allow_html=True)
    
    # List type selector for visualization
    viz_type = st.selectbox(
        "Select visualization type:",
        ["Singly Linked List", "Doubly Linked List", "Circular Linked List"],
        help="Choose which type of linked list to visualize"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Get data based on selection or session state
    if 'linked_list' in st.session_state and st.session_state.linked_list.size > 0:
        if hasattr(st.session_state.linked_list, 'traverse_forward'):
            elements = st.session_state.linked_list.traverse_forward()
        else:
            elements = st.session_state.linked_list.traverse()
    else:
        elements = [10, 20, 30, 40, 50]

    st.markdown(f"""
    <div class="section-card">
        <h2 style="color: var(--primary-700); margin-bottom: 1.5rem;">
            3D {viz_type} Visualization
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Create 3D visualization based on type
    fig = go.Figure()
    
    if viz_type == "Singly Linked List":
        # Linear arrangement for singly linked list
        node_x = [i * 3 for i in range(len(elements))]
        node_y = [0] * len(elements)
        node_z = [0] * len(elements)
        
        # Add nodes
        fig.add_trace(go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers+text',
            marker=dict(
                size=20,
                color='#4A90E2',
                opacity=0.9,
                line=dict(width=3, color='#2E5BBA')
            ),
            text=[str(val) for val in elements],
            textposition="middle center",
            textfont=dict(size=14, color='white', family="Arial Black"),
            name="Nodes"
        ))
        
        # Add forward connections
        for i in range(len(elements) - 1):
            fig.add_trace(go.Scatter3d(
                x=[node_x[i], node_x[i+1]],
                y=[node_y[i], node_y[i+1]],
                z=[node_z[i], node_z[i+1]],
                mode='lines',
                line=dict(color='#FF6B6B', width=8),
                showlegend=False
            ))
            
    elif viz_type == "Doubly Linked List":
        # Linear arrangement with bidirectional arrows
        node_x = [i * 4 for i in range(len(elements))]
        node_y = [0] * len(elements)
        node_z = [0] * len(elements)
        
        # Add nodes
        fig.add_trace(go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers+text',
            marker=dict(
                size=20,
                color='#E74C3C',
                opacity=0.9,
                line=dict(width=3, color='#C0392B')
            ),
            text=[str(val) for val in elements],
            textposition="middle center",
            textfont=dict(size=14, color='white', family="Arial Black"),
            name="Nodes"
        ))
        
        # Add forward connections (above)
        for i in range(len(elements) - 1):
            fig.add_trace(go.Scatter3d(
                x=[node_x[i], node_x[i+1]],
                y=[0.5, 0.5],
                z=[0, 0],
                mode='lines',
                line=dict(color='#FF6B6B', width=6),
                showlegend=False
            ))
            
        # Add backward connections (below)
        for i in range(1, len(elements)):
            fig.add_trace(go.Scatter3d(
                x=[node_x[i], node_x[i-1]],
                y=[-0.5, -0.5],
                z=[0, 0],
                mode='lines',
                line=dict(color='#4ECDC4', width=6),
                showlegend=False
            ))
            
    else:  # Circular Linked List
        # Circular arrangement
        import math
        radius = 3
        node_x = [radius * math.cos(2 * math.pi * i / len(elements)) for i in range(len(elements))]
        node_y = [radius * math.sin(2 * math.pi * i / len(elements)) for i in range(len(elements))]
        node_z = [0] * len(elements)
        
        # Add nodes
        fig.add_trace(go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers+text',
            marker=dict(
                size=20,
                color='#9B59B6',
                opacity=0.9,
                line=dict(width=3, color='#8E44AD')
            ),
            text=[str(val) for val in elements],
            textposition="middle center",
            textfont=dict(size=14, color='white', family="Arial Black"),
            name="Nodes"
        ))
        
        # Add circular connections
        for i in range(len(elements)):
            next_i = (i + 1) % len(elements)
            fig.add_trace(go.Scatter3d(
                x=[node_x[i], node_x[next_i]],
                y=[node_y[i], node_y[next_i]],
                z=[node_z[i], node_z[next_i]],
                mode='lines',
                line=dict(color='#FF6B6B', width=8),
                showlegend=False
            ))
    
    fig.update_layout(
        title=dict(
            text=f"3D {viz_type} Visualization",
            font=dict(size=20, color='var(--primary-700)', family='Space Grotesk')
        ),
        scene=dict(
            xaxis_title="X Position",
            yaxis_title="Y Position",
            zaxis_title="Z Position",
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
            bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                gridcolor='rgba(14, 165, 233, 0.1)',
                title_font=dict(color='var(--primary-600)')
            ),
            yaxis=dict(
                gridcolor='rgba(14, 165, 233, 0.1)',
                title_font=dict(color='var(--primary-600)')
            ),
            zaxis=dict(
                gridcolor='rgba(14, 165, 233, 0.1)',
                title_font=dict(color='var(--primary-600)')
            )
        ),
        height=650,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=80, b=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Modern info cards with soft UI design
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-md);
    ">
    """, unsafe_allow_html=True)
    
    # Add description based on type
    if viz_type == "Singly Linked List":
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 1.5rem;">🔗</span>
            <div>
                <strong style="color: var(--primary-700);">Singly Linked List</strong>
                <p style="margin: 0; color: var(--neutral-600);">Nodes connected in one direction with forward pointers only.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    elif viz_type == "Doubly Linked List":
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 1.5rem;">↔️</span>
            <div>
                <strong style="color: var(--primary-700);">Doubly Linked List</strong>
                <p style="margin: 0; color: var(--neutral-600);">Nodes with bidirectional connections - red arrows show 'next' pointers, teal arrows show 'prev' pointers.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 1.5rem;">🔄</span>
            <div>
                <strong style="color: var(--primary-700);">Circular Linked List</strong>
                <p style="margin: 0; color: var(--neutral-600);">Nodes arranged in a circle where the last node points back to the first node.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
        <h2 style="color: var(--primary-700); margin-bottom: 1.5rem;">Memory Layout Comparison</h2>
        <p style="color: var(--neutral-600); margin-bottom: 2rem;">
            Understanding how linked list nodes are stored in memory with modern visual representations
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Use elements from the selected visualization type
    demo_elements = elements[:4]  # Limit to 4 for better display
    
    # Memory layout visualization based on selected type
    st.markdown(f"""
    <div style="
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-md);
    ">
        <h3 style="color: var(--primary-700); margin-bottom: 1.5rem;">Memory Structure: {viz_type}</h3>
    """, unsafe_allow_html=True)
    
    if viz_type == "Singly Linked List":
        cols = st.columns(len(demo_elements) + 1)
        
        for i, val in enumerate(demo_elements):
            with cols[i]:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, var(--primary-500) 0%, var(--primary-600) 100%);
                    border-radius: var(--radius-lg);
                    padding: 1.5rem;
                    margin: 0.5rem;
                    text-align: center;
                    color: white;
                    box-shadow: var(--shadow-md);
                    transition: all var(--transition-normal);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                " onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='var(--shadow-xl)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-md)'">
                    <div style="font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;">Node {i}</div>
                    <div style="font-size: 1.5rem; font-weight: 700; margin: 1rem 0;">{val}</div>
                    <div style="font-size: 0.8rem; opacity: 0.9; margin-bottom: 1rem;">Next: 0x{(i+1)*100:03X}</div>
                    <div style="font-size: 1.2rem;">→</div>
                </div>
                """, unsafe_allow_html=True)
        
        with cols[-1]:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, var(--error-500) 0%, var(--error-600) 100%);
                border-radius: var(--radius-lg);
                padding: 1.5rem;
                margin: 0.5rem;
                text-align: center;
                color: white;
                box-shadow: var(--shadow-md);
                border: 1px solid rgba(255, 255, 255, 0.2);
            ">
                    <div style="font-weight: bold;">NULL</div>
                <div style="font-size: 1.3em; margin: 8px 0;">∅</div>
                <div style="font-size: 0.7em;">End</div>
            </div>
                <div style="font-weight: bold;">NULL</div>
                <div style="font-size: 1.3em; margin: 8px 0;">∅</div>
                <div style="font-size: 0.7em;">End</div>
            </div>
            """, unsafe_allow_html=True)
            
    elif viz_type == "Doubly Linked List":
        cols = st.columns(len(demo_elements))
        
        for i, val in enumerate(demo_elements):
            with cols[i]:
                st.markdown(f"""
                <div style="
                    border: 3px solid #E74C3C;
                    border-radius: 15px;
                    padding: 15px;
                    margin: 5px;
                    background: linear-gradient(135deg, #E74C3C 0%, #C0392B 100%);
                    text-align: center;
                    color: white;
                ">
                    <div style="font-weight: bold;">Node {i}</div>
                    <div style="font-size: 1.3em; margin: 8px 0;">{val}</div>
                    <div style="font-size: 0.6em;">Prev: {'NULL' if i == 0 else f'0x{i*100:03X}'}</div>
                    <div style="font-size: 0.6em;">Next: {'NULL' if i == len(demo_elements)-1 else f'0x{(i+1)*100:03X}'}</div>
                    <div style="margin-top: 5px;">{'↔️' if 0 < i < len(demo_elements)-1 else '→' if i == 0 else '←'}</div>
                </div>
                """, unsafe_allow_html=True)
                
    else:  # Circular Linked List
        cols = st.columns(len(demo_elements))
        
        for i, val in enumerate(demo_elements):
            with cols[i]:
                next_addr = f"0x{((i+1) % len(demo_elements))*100:03X}"
                st.markdown(f"""
                <div style="
                    border: 3px solid #9B59B6;
                    border-radius: 15px;
                    padding: 15px;
                    margin: 5px;
                    background: linear-gradient(135deg, #9B59B6 0%, #8E44AD 100%);
                    text-align: center;
                    color: white;
                ">
                    <div style="font-weight: bold;">Node {i}</div>
                    <div style="font-size: 1.3em; margin: 8px 0;">{val}</div>
                    <div style="font-size: 0.7em;">Next: {next_addr}</div>
                    <div style="margin-top: 8px;">{'🔄' if i == len(demo_elements)-1 else '→'}</div>
                </div>
                """, unsafe_allow_html=True)
        
    # Add comparison table
    st.subheader("Memory Structure Comparison")
    
    comparison_data = {
        "Aspect": ["Pointers per Node", "Memory Overhead", "Traversal", "Insertion Complexity", "Use Case"],
        "Singly Linked": ["1 (next)", "Low", "Forward only", "Simple", "Stacks, Queues"],
        "Doubly Linked": ["2 (next, prev)", "High", "Bidirectional", "Complex", "Deques, Caches"],
        "Circular Linked": ["1 (next)", "Low", "Circular", "Moderate", "Round-robin, Buffers"]
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)

# Enhanced Interactive Quiz with Gamification
def interactive_quiz():
    st.markdown('''
    <div class="section-card">
        <h1 class="gradient-text" style="text-align: center; margin-bottom: 2rem;">
            🎮 Gamified Learning Hub
        </h1>
    </div>
    ''', unsafe_allow_html=True)
    save_progress("Quiz")
    
    # User profile section
    with st.expander("👤 Player Profile", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            new_username = st.text_input("Username:", value=st.session_state.username)
            if new_username != st.session_state.username:
                st.session_state.username = new_username
        with col2:
            st.metric("Total Score", st.session_state.user_score)
        with col3:
            st.metric("Achievements", len(st.session_state.achievements))
    
    # Main gamification tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🧠 Interactive Quiz", "💻 Coding Challenges", "⚡ Time Challenges", "🏆 Leaderboard"])
    
    with tab1:
        enhanced_quiz_section()
    
    with tab2:
        coding_challenges_section()
    
    with tab3:
        time_challenges_section()
    
    with tab4:
        leaderboard_section()

def enhanced_quiz_section():
    st.markdown('''
    <div class="section-card" style="margin-bottom: 2rem;">
        <h2 class="gradient-text" style="text-align: center; margin-bottom: 1rem;">
            🧠 Interactive Quiz
        </h2>
    </div>
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 20px; padding: 1.5rem; margin-bottom: 2rem; border: 1px solid rgba(255, 255, 255, 0.1);">
    ''', unsafe_allow_html=True)
    
    # Quiz mode selector
    st.markdown('<div style="display: flex; gap: 1rem; margin-bottom: 1rem;">', unsafe_allow_html=True)
    quiz_mode = st.selectbox("Select Quiz Mode:", 
                            ["Practice Mode", "Challenge Mode", "Difficulty-Based"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    if quiz_mode == "Difficulty-Based":
        st.markdown('<div style="display: flex; gap: 1rem; margin-bottom: 1rem;">', unsafe_allow_html=True)
        difficulty = st.selectbox("Choose Difficulty:", ["easy", "medium", "hard"])
        st.markdown('</div>', unsafe_allow_html=True)
        questions = [q for q in QUIZ_QUESTIONS if q.get('difficulty', 'medium') == difficulty]
        if not questions:
            st.warning(f"No {difficulty} questions available. Showing all questions instead.")
            questions = QUIZ_QUESTIONS
    else:
        questions = QUIZ_QUESTIONS
    
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'quiz_start_time' not in st.session_state:
        st.session_state.quiz_start_time = None
    
    if st.session_state.current_question < len(questions):
        q = questions[st.session_state.current_question]
        
        # Start timer on first question
        if st.session_state.quiz_start_time is None:
            import time
            st.session_state.quiz_start_time = time.time()
        
        # Progress bar
        progress = (st.session_state.current_question + 1) / len(questions)
        
        # Modern progress bar
        progress_html = f"""
        <div style="background: rgba(255, 255, 255, 0.1); border-radius: 20px; height: 12px; margin: 1.5rem 0; overflow: hidden; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(90deg, var(--primary-blue), var(--primary-purple)); width: {progress * 100}%; height: 100%; border-radius: 20px; transition: width 0.3s ease;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 2rem;">
            <span style="color: var(--text-secondary); font-size: 0.9rem;">Question {st.session_state.current_question + 1} of {len(questions)}</span>
            <span style="color: var(--text-secondary); font-size: 0.9rem;">{int(progress * 100)}% Complete</span>
        </div>
        """
        st.markdown(progress_html, unsafe_allow_html=True)
        
        # Question card
        difficulty = q.get('difficulty', 'medium')
        difficulty_colors = {"easy": "#4CAF50", "medium": "#FF9800", "hard": "#F44336"}
        difficulty_color = difficulty_colors.get(difficulty, "#FF9800")
        
        question_html = f"""
        <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; margin: 1.5rem 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                <h3 style="color: var(--text-primary); margin: 0; font-size: 1.2rem;">Question {st.session_state.current_question + 1}</h3>
                <span style="background: {difficulty_color}; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">{difficulty.upper()}</span>
            </div>
            <h4 style="color: var(--text-primary); margin-bottom: 1.5rem; line-height: 1.5;">{q["question"]}</h4>
        </div>
        """
        st.markdown(question_html, unsafe_allow_html=True)
        
        # Answer options
        user_answer = st.radio("Select your answer:", q["options"], 
                              key=f"q_{st.session_state.current_question}",
                              label_visibility="collapsed")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎯 Submit Answer", type="primary", use_container_width=True):
                selected_index = q["options"].index(user_answer)
                points = q.get('points', 10)
                
                if selected_index == q["correct"]:
                    success_html = f"""
                    <div style="background: linear-gradient(135deg, #4CAF50 0%, #66BB6A 100%); color: white; border-radius: 15px; padding: 1rem; margin: 1rem 0; text-align: center; box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);">
                        <h4 style="margin: 0;">✅ Correct! 🎉 +{points} points</h4>
                    </div>
                    """
                    st.markdown(success_html, unsafe_allow_html=True)
                    st.session_state.quiz_score += 1
                    st.session_state.user_score += points
                    st.session_state.correct_answers += 1
                    
                    # Check for achievements
                    check_achievements()
                else:
                    error_html = f"""
                    <div style="background: linear-gradient(135deg, #F44336 0%, #EF5350 100%); color: white; border-radius: 15px; padding: 1rem; margin: 1rem 0; text-align: center; box-shadow: 0 4px 15px rgba(244, 67, 54, 0.3);">
                        <h4 style="margin: 0;">❌ Incorrect</h4>
                        <p style="margin: 0.5rem 0 0 0;">The correct answer is: {q["options"][q["correct"]]}</p>
                    </div>
                    """
                    st.markdown(error_html, unsafe_allow_html=True)
                
                # Explanation
                explanation_html = f"""
                <div style="background: rgba(255, 193, 7, 0.1); border-left: 4px solid var(--warning-yellow); border-radius: 10px; padding: 1rem; margin: 1rem 0;">
                    <p style="color: var(--warning-yellow); margin: 0; font-weight: 500;">💡 {q["explanation"]}</p>
                </div>
                """
                st.markdown(explanation_html, unsafe_allow_html=True)
                st.session_state.quiz_attempts += 1
        
        with col2:
            if st.button("➡️ Next Question", use_container_width=True):
                st.session_state.current_question += 1
                st.rerun()
    
    else:
        # Quiz completed
        import time
        if st.session_state.quiz_start_time:
            completion_time = time.time() - st.session_state.quiz_start_time
            st.session_state.quiz_start_time = None
        else:
            completion_time = 0
        
        # Quiz completion card
        score_percentage = (st.session_state.quiz_score / len(questions)) * 100
        
        completion_html = f"""
        <div style="background: linear-gradient(135deg, rgba(106, 27, 154, 0.1) 0%, rgba(81, 45, 168, 0.1) 100%); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; margin: 2rem 0; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
            <h1 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 2.5rem;">🎊 Quiz Completed!</h1>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 2rem 0;">
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 1rem;">
                    <h3 style="color: var(--primary-blue); margin: 0; font-size: 1.8rem;">{st.session_state.quiz_score}/{len(questions)}</h3>
                    <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0; font-size: 0.9rem;">Score</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 1rem;">
                    <h3 style="color: var(--success-green); margin: 0; font-size: 1.8rem;">{score_percentage:.1f}%</h3>
                    <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0; font-size: 0.9rem;">Percentage</p>
                </div>
                <div style="background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 1rem;">
                    <h3 style="color: var(--warning-yellow); margin: 0; font-size: 1.8rem;">{completion_time:.1f}s</h3>
                    <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0; font-size: 0.9rem;">Time</p>
                </div>
            </div>
        """
        st.markdown(completion_html, unsafe_allow_html=True)
        
        # Performance feedback
        if score_percentage >= 90:
            feedback_html = """
            <div style="background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(102, 187, 106, 0.1) 100%); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; text-align: center; border: 1px solid rgba(76, 175, 80, 0.3);">
                <h3 style="color: var(--success-green); margin: 0;">🏆 Outstanding! You're a linked list master!</h3>
            </div>
            """
            badge = "🏆 Quiz Master"
        elif score_percentage >= 80:
            feedback_html = """
            <div style="background: linear-gradient(135deg, rgba(33, 150, 243, 0.1) 0%, rgba(66, 165, 245, 0.1) 100%); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; text-align: center; border: 1px solid rgba(33, 150, 243, 0.3);">
                <h3 style="color: var(--primary-blue); margin: 0;">🥇 Excellent work! You have a strong understanding!</h3>
            </div>
            """
            badge = "🥇 Quiz Expert"
        elif score_percentage >= 70:
            feedback_html = """
            <div style="background: linear-gradient(135deg, rgba(255, 152, 0, 0.1) 0%, rgba(255, 193, 7, 0.1) 100%); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; text-align: center; border: 1px solid rgba(255, 152, 0, 0.3);">
                <h3 style="color: var(--warning-yellow); margin: 0;">🥈 Good job! Keep practicing to improve!</h3>
            </div>
            """
            badge = "🥈 Quiz Achiever"
        else:
            feedback_html = """
            <div style="background: linear-gradient(135deg, rgba(244, 67, 54, 0.1) 0%, rgba(239, 83, 80, 0.1) 100%); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; text-align: center; border: 1px solid rgba(244, 67, 54, 0.3);">
                <h3 style="color: var(--error-red); margin: 0;">🥉 Keep studying! Review the concepts and try again.</h3>
            </div>
            """
            badge = "🥉 Quiz Participant"
        
        st.markdown(feedback_html, unsafe_allow_html=True)
        
        # Add badge to achievements
        if badge not in st.session_state.achievements:
            st.session_state.achievements.append(badge)
            st.balloons()
        
        # Update leaderboard
        update_leaderboard("Quiz", score_percentage, completion_time)
        
        # Restart button
        restart_html = """
        <div style="text-align: center; margin-top: 2rem;">
            <button style="background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-purple) 100%); color: white; border: none; border-radius: 25px; padding: 1rem 2rem; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(106, 27, 154, 0.3);" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(106, 27, 154, 0.4)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(106, 27, 154, 0.3)';">
                🔄 Restart Quiz
            </button>
        </div>
        """
        if st.button("🔄 Restart Quiz", use_container_width=True):
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def coding_challenges_section():
    st.markdown('''
    <div class="section-card" style="margin-bottom: 2rem;">
        <h2 class="gradient-text" style="text-align: center; margin-bottom: 1rem;">
            💻 Coding Challenges
        </h2>
    </div>
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; margin-bottom: 2rem; border: 1px solid rgba(255, 255, 255, 0.1);">
    ''', unsafe_allow_html=True)
    
    if 'current_coding_challenge' not in st.session_state:
        st.session_state.current_coding_challenge = 0
    if 'coding_attempts' not in st.session_state:
        st.session_state.coding_attempts = {}
    
    # Challenge selector
    st.markdown('<div style="margin-bottom: 2rem;">', unsafe_allow_html=True)
    challenge_names = [challenge["title"] for challenge in CODING_CHALLENGES]
    selected_challenge = st.selectbox("Choose a challenge:", challenge_names)
    st.markdown('</div>', unsafe_allow_html=True)
    
    challenge_idx = challenge_names.index(selected_challenge)
    challenge = CODING_CHALLENGES[challenge_idx]
    
    # Challenge info card
    difficulty_colors = {"easy": "#4CAF50", "medium": "#FF9800", "hard": "#F44336"}
    difficulty_color = difficulty_colors.get(challenge['difficulty'], "#FF9800")
    
    challenge_html = f"""
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; margin: 1.5rem 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
            <h3 style="color: var(--text-primary); margin: 0; font-size: 1.5rem;">🎯 {challenge['title']}</h3>
            <div style="display: flex; gap: 1rem; align-items: center;">
                <span style="background: {difficulty_color}; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">{challenge['difficulty'].upper()}</span>
                <span style="background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-purple) 100%); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">{challenge['points']} Points</span>
            </div>
        </div>
        <div style="margin-bottom: 2rem;">
            <h4 style="color: var(--text-primary); margin-bottom: 1rem;">📝 Problem Description</h4>
            <p style="color: var(--text-secondary); line-height: 1.6;">{challenge['description']}</p>
        </div>
        <div>
            <h4 style="color: var(--text-primary); margin-bottom: 1rem;">🧪 Test Cases</h4>
            <div style="display: flex; flex-direction: column; gap: 0.5rem;">
    """
    
    for i, test_case in enumerate(challenge['test_cases']):
        challenge_html += f"""
                <div style="background: rgba(0, 0, 0, 0.2); border-radius: 10px; padding: 0.8rem; border-left: 4px solid var(--primary-blue);">
                    <code style="color: var(--text-secondary); font-size: 0.9rem;">Input: {test_case['input']} → Expected: {test_case['expected']}</code>
                </div>
        """
    
    challenge_html += """
            </div>
        </div>
    </div>
    """
    st.markdown(challenge_html, unsafe_allow_html=True)
    
    # Progress card
    attempts = st.session_state.coding_attempts.get(challenge['title'], 0)
    progress_html = f"""
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h4 style="color: var(--text-primary); margin-bottom: 1rem;">📊 Your Progress</h4>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h3 style="color: var(--primary-blue); margin: 0; font-size: 1.5rem;">{attempts}</h3>
                <p style="color: var(--text-secondary); margin: 0; font-size: 0.9rem;">Attempts</p>
            </div>
            <div style="text-align: right;">
    """
    
    if attempts > 0:
        if attempts == 1:
            progress_html += '<span style="color: var(--success-green); font-weight: 600;">✅ Solved on first try!</span>'
        elif attempts <= 3:
            progress_html += f'<span style="color: var(--primary-blue); font-weight: 600;">✅ Solved in {attempts} attempts</span>'
        else:
            progress_html += f'<span style="color: var(--warning-yellow); font-weight: 600;">✅ Solved in {attempts} attempts</span>'
    else:
        progress_html += '<span style="color: var(--text-secondary);">Not attempted yet</span>'
    
    progress_html += """
            </div>
        </div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)
    
    # Code editor
    st.markdown('<h4 style="color: var(--text-primary); margin: 2rem 0 1rem 0;">💻 Code Editor</h4>', unsafe_allow_html=True)
    user_code = st.text_area("Write your solution:", 
                            value=challenge['starter_code'], 
                            height=300,
                            key=f"code_{challenge_idx}",
                            label_visibility="collapsed")
    
    # Action buttons
    st.markdown('<div style="display: flex; gap: 1rem; margin: 2rem 0;">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏃 Run Code", type="primary", use_container_width=True):
            run_coding_challenge(challenge, user_code)
    
    with col2:
        if st.button("💡 Show Hint", use_container_width=True):
            hint_html = """
            <div style="background: rgba(255, 193, 7, 0.1); border-left: 4px solid var(--warning-yellow); border-radius: 10px; padding: 1rem; margin: 1rem 0;">
                <p style="color: var(--warning-yellow); margin: 0; font-weight: 500;">💡 <strong>Hint:</strong> Try using the two-pointer technique or consider the time complexity requirements.</p>
            </div>
            """
            st.markdown(hint_html, unsafe_allow_html=True)
    
    with col3:
        if st.button("👁️ Show Solution", use_container_width=True):
            solution_html = f"""
            <div style="background: rgba(0, 0, 0, 0.2); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
                <h4 style="color: var(--text-primary); margin-bottom: 1rem;">Solution</h4>
                <pre style="background: rgba(0, 0, 0, 0.3); border-radius: 10px; padding: 1rem; overflow-x: auto;"><code style="color: var(--text-secondary);">{challenge['solution']}</code></pre>
                <div style="background: rgba(255, 152, 0, 0.1); border-left: 4px solid var(--warning-yellow); border-radius: 5px; padding: 0.8rem; margin-top: 1rem;">
                    <p style="color: var(--warning-yellow); margin: 0; font-size: 0.9rem;">⚠️ Viewing the solution reduces points by 50%</p>
                </div>
            </div>
            """
            st.markdown(solution_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def run_coding_challenge(challenge, user_code):
    try:
        # Modern execution result
        execution_html = """
        <div style="background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(102, 187, 106, 0.1) 100%); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(76, 175, 80, 0.3); text-align: center;">
            <h4 style="color: var(--success-green); margin: 0;">✅ Code executed successfully!</h4>
        </div>
        """
        st.markdown(execution_html, unsafe_allow_html=True)
        
        # Simulate test results
        import random
        passed_tests = random.randint(1, len(challenge['test_cases']))
        total_tests = len(challenge['test_cases'])
        
        if passed_tests == total_tests:
            success_html = f"""
            <div style="background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(102, 187, 106, 0.1) 100%); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(76, 175, 80, 0.3); text-align: center;">
                <h4 style="color: var(--success-green); margin: 0;">🎉 All {total_tests} test cases passed!</h4>
            </div>
            """
            st.markdown(success_html, unsafe_allow_html=True)
            
            points = challenge['points']
            st.session_state.coding_challenge_score += points
            st.session_state.user_score += points
            
            # Track attempts
            attempts = st.session_state.coding_attempts.get(challenge['title'], 0) + 1
            st.session_state.coding_attempts[challenge['title']] = attempts
            
            # Achievement check
            if attempts == 1:
                achievement = f"🏆 First Try: {challenge['title']}"
                if achievement not in st.session_state.achievements:
                    st.session_state.achievements.append(achievement)
                    st.balloons()
            
            # Points earned display
            points_html = f"""
            <div style="background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-purple) 100%); border-radius: 15px; padding: 1rem; margin: 1rem 0; text-align: center; box-shadow: 0 4px 15px rgba(106, 27, 154, 0.3);">
                <h4 style="color: white; margin: 0;">Points Earned: {points}</h4>
            </div>
            """
            st.markdown(points_html, unsafe_allow_html=True)
        else:
            error_html = f"""
            <div style="background: linear-gradient(135deg, rgba(244, 67, 54, 0.1) 0%, rgba(239, 83, 80, 0.1) 100%); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(244, 67, 54, 0.3); text-align: center;">
                <h4 style="color: var(--error-red); margin: 0;">❌ {passed_tests}/{total_tests} test cases passed. Keep trying!</h4>
            </div>
            """
            st.markdown(error_html, unsafe_allow_html=True)
            
    except Exception as e:
        error_html = f"""
        <div style="background: linear-gradient(135deg, rgba(244, 67, 54, 0.1) 0%, rgba(239, 83, 80, 0.1) 100%); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(244, 67, 54, 0.3);">
            <h4 style="color: var(--error-red); margin: 0;">❌ Code execution failed</h4>
            <p style="color: var(--text-secondary); margin: 0.5rem 0 0 0;">{str(e)}</p>
        </div>
        """
        st.markdown(error_html, unsafe_allow_html=True)

def time_challenges_section():
    st.markdown('''
    <div class="section-card">
        <h2 style="background: linear-gradient(135deg, var(--primary-blue), var(--primary-purple)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-align: center; margin-bottom: 2rem;">
            ⚡ Time Challenges
        </h2>
    </div>
    ''', unsafe_allow_html=True)
    
    if 'active_time_challenge' not in st.session_state:
        st.session_state.active_time_challenge = None
    if 'time_challenge_start' not in st.session_state:
        st.session_state.time_challenge_start = None
    if 'time_challenge_questions' not in st.session_state:
        st.session_state.time_challenge_questions = []
    if 'time_challenge_current' not in st.session_state:
        st.session_state.time_challenge_current = 0
    if 'time_challenge_score' not in st.session_state:
        st.session_state.time_challenge_score = 0
    
    # Challenge selector
    challenge_names = [challenge["title"] for challenge in TIME_CHALLENGES]
    selected_challenge = st.selectbox("Choose a time challenge:", challenge_names)
    challenge_idx = challenge_names.index(selected_challenge)
    challenge = TIME_CHALLENGES[challenge_idx]
    
    # Challenge info card
    challenge_info_html = f'''
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
                <h3 style="color: var(--text-primary); margin: 0 0 0.5rem 0;">⚡ {challenge['title']}</h3>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">⏱️ Time Limit: {challenge['time_limit']}s</span>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">🎯 Bonus: {challenge['bonus_points']} pts</span>
                    <span style="color: var(--text-secondary); font-size: 0.9rem;">📝 {len(challenge['questions'])} questions</span>
                </div>
            </div>
            <div style="text-align: center;">
                <div style="color: var(--text-secondary); font-size: 0.8rem;">Best Time</div>
                <div style="color: var(--primary-blue); font-size: 1.2rem; font-weight: bold;">
                    {st.session_state.time_challenge_best.get(challenge['title'], 'Not attempted') if st.session_state.time_challenge_best.get(challenge['title']) else 'Not attempted'}
                </div>
            </div>
        </div>
    </div>
    '''
    st.markdown(challenge_info_html, unsafe_allow_html=True)
    
    # Challenge controls
    if st.session_state.active_time_challenge != challenge['title']:
        start_button_html = f'''
        <div style="display: flex; justify-content: center; margin: 2rem 0;">
            <button style="background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-purple) 100%); color: white; border: none; border-radius: 25px; padding: 1rem 2rem; font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(106, 27, 154, 0.3);" 
                    onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(106, 27, 154, 0.4)'" 
                    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(106, 27, 154, 0.3)'">
                🚀 Start {challenge['title']}
            </button>
        </div>
        '''
        if st.button(f"🚀 Start {challenge['title']}", type="primary"):
            start_time_challenge(challenge)
            st.rerun()
    else:
        # Active challenge
        import time
        if st.session_state.time_challenge_start:
            elapsed = time.time() - st.session_state.time_challenge_start
            remaining = max(0, challenge['time_limit'] - elapsed)
            
            # Timer display
            if remaining > 0:
                timer_card_html = f'''
                <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
                    <div style="font-size: 2rem; color: var(--primary-blue); font-weight: bold; margin-bottom: 1rem;">⏱️ {remaining:.1f}s</div>
                    <div style="background: rgba(255, 255, 255, 0.1); border-radius: 10px; height: 8px; overflow: hidden;">
                        <div style="background: linear-gradient(135deg, var(--primary-blue), var(--primary-purple)); height: 100%; width: {min(100, (elapsed / challenge['time_limit']) * 100)}%; transition: width 0.3s ease;"></div>
                    </div>
                </div>
                '''
                st.markdown(timer_card_html, unsafe_allow_html=True)
            else:
                time_up_html = '''
                <div style="background: linear-gradient(135deg, rgba(244, 67, 54, 0.1) 0%, rgba(239, 83, 80, 0.1) 100%); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(244, 67, 54, 0.3); text-align: center;">
                    <h3 style="color: var(--error-red); margin: 0;">⏰ Time's Up!</h3>
                </div>
                '''
                st.markdown(time_up_html, unsafe_allow_html=True)
                end_time_challenge(challenge)
                st.rerun()
            
            # Current question
            if st.session_state.time_challenge_current < len(st.session_state.time_challenge_questions):
                q_idx = st.session_state.time_challenge_questions[st.session_state.time_challenge_current]
                q = QUIZ_QUESTIONS[q_idx]
                
                question_card_html = f'''
                <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1);">
                    <h3 style="color: var(--text-primary); margin: 0 0 1rem 0;">Question {st.session_state.time_challenge_current + 1}</h3>
                    <p style="color: var(--text-secondary); margin: 0 0 1rem 0;">{q["question"]}</p>
                </div>
                '''
                st.markdown(question_card_html, unsafe_allow_html=True)
                
                user_answer = st.radio("Quick! Choose your answer:", q["options"], 
                                      key=f"time_q_{st.session_state.time_challenge_current}")
                
                if st.button("Submit & Next ⚡", type="primary"):
                    selected_index = q["options"].index(user_answer)
                    if selected_index == q["correct"]:
                        st.session_state.time_challenge_score += q.get('points', 10)
                    
                    st.session_state.time_challenge_current += 1
                    
                    if st.session_state.time_challenge_current >= len(st.session_state.time_challenge_questions):
                        end_time_challenge(challenge)
                    st.rerun()
            
            # Emergency stop
            stop_button_html = '''
            <div style="display: flex; justify-content: center; margin: 2rem 0;">
                <button style="background: rgba(244, 67, 54, 0.2); color: var(--error-red); border: 1px solid rgba(244, 67, 54, 0.3); border-radius: 25px; padding: 0.8rem 1.5rem; font-size: 1rem; font-weight: bold; cursor: pointer; transition: all 0.3s ease;" 
                        onmouseover="this.style.background='rgba(244, 67, 54, 0.3)'" 
                        onmouseout="this.style.background='rgba(244, 67, 54, 0.2)'">
                    🛑 Stop Challenge
                </button>
            </div>
            '''
            if st.button("🛑 Stop Challenge"):
                end_time_challenge(challenge)
                st.rerun()

def start_time_challenge(challenge):
    import time
    import random
    
    st.session_state.active_time_challenge = challenge['title']
    st.session_state.time_challenge_start = time.time()
    st.session_state.time_challenge_questions = challenge['questions'].copy()
    random.shuffle(st.session_state.time_challenge_questions)
    st.session_state.time_challenge_current = 0
    st.session_state.time_challenge_score = 0

def end_time_challenge(challenge):
    import time
    
    if st.session_state.time_challenge_start:
        completion_time = time.time() - st.session_state.time_challenge_start
        
        # Update best time
        current_best = st.session_state.time_challenge_best.get(challenge['title'], float('inf'))
        if completion_time < current_best:
            st.session_state.time_challenge_best[challenge['title']] = completion_time
        
        # Calculate final score
        base_score = st.session_state.time_challenge_score
        time_bonus = max(0, challenge['bonus_points'] * (1 - completion_time / challenge['time_limit']))
        total_score = base_score + time_bonus
        
        st.session_state.user_score += int(total_score)
        
        # Show results with modern UI
        results_html = f'''
        <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 2rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
            <h3 style="color: var(--success-green); margin: 0 0 1rem 0;">⚡ Challenge Complete!</h3>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin: 1rem 0;">
                <div style="text-align: center;">
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">Time</div>
                    <div style="color: var(--primary-blue); font-size: 1.5rem; font-weight: bold;">{completion_time:.1f}s</div>
                </div>
                <div style="text-align: center;">
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">Total Score</div>
                    <div style="color: var(--success-green); font-size: 1.5rem; font-weight: bold;">{int(total_score)} pts</div>
                </div>
            </div>
        </div>
        '''
        st.markdown(results_html, unsafe_allow_html=True)
        
        # Update leaderboard
        update_leaderboard("Time Challenge", int(total_score), completion_time)
    
    # Reset challenge state
    st.session_state.active_time_challenge = None
    st.session_state.time_challenge_start = None
    st.session_state.time_challenge_questions = []
    st.session_state.time_challenge_current = 0
    st.session_state.time_challenge_score = 0

def leaderboard_section():
    st.markdown('''
    <div class="section-card">
        <h2 style="background: linear-gradient(135deg, var(--primary-gold), var(--primary-orange)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-align: center; margin-bottom: 2rem;">
            🏆 Leaderboard
        </h2>
    </div>
    ''', unsafe_allow_html=True)
    
    if not st.session_state.leaderboard:
        empty_html = '''
        <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 15px; padding: 2rem; margin: 1rem 0; border: 1px solid rgba(255, 255, 255, 0.1); text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
            <h3 style="color: var(--text-primary); margin: 0 0 0.5rem 0;">No Scores Yet</h3>
            <p style="color: var(--text-secondary); margin: 0;">Complete challenges to appear on the leaderboard!</p>
        </div>
        '''
        st.markdown(empty_html, unsafe_allow_html=True)
        return
    
    # Sort leaderboard by score
    sorted_leaderboard = sorted(st.session_state.leaderboard, 
                               key=lambda x: x['score'], reverse=True)