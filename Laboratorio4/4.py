class BrowserHistory:
    """Simple browser history implementation using stacks."""
    def __init__(self):
        """Initialize browser history with back and forward stacks."""
        self.back_stack = []  # Stack for back navigation
        self.forward_stack = []  # Stack for forward navigation
        self.current_page = None
    
    def visit(self, url):
        """Visit a new page, adding current to back stack and clearing forward stack."""
        if self.current_page:
            self.back_stack.append(self.current_page)
        
        self.current_page = url
        self.forward_stack = []  # Clear forward history
        
        return f"Visited: {url}"
    
    def back(self):
        """Navigate back in history."""
        if not self.back_stack:
            return "No back history"
        
        # Move current page to forward stack
        self.forward_stack.append(self.current_page)
        # Set current page to the last back page
        self.current_page = self.back_stack.pop()
        
        return f"Navigated back to: {self.current_page}" 
    def forward(self):
        """Navigate forward in history."""
        if not self.forward_stack:
            return "No forward history"
        
        # Move current page to back stack
        self.back_stack.append(self.current_page)
        # Set current page to the last forward page
        self.current_page = self.forward_stack.pop()
        
        return f"Navigated forward to: {self.current_page}"
    
    def get_current(self):
        """Get the current page."""
        if not self.current_page:
            return "No current page"
        
        return f"Current page: {self.current_page}"

def test_browser_history():
    """Test browser navigation with back and forward operations."""
    print("Testing browser navigation:")
    browser = BrowserHistory()
    
    print(browser.get_current())
    
    # Visit some pages
    print(browser.visit("https://www.example.com"))
    print(browser.visit("https://www.example.com/page1"))
    print(browser.visit("https://www.example.com/page2"))
    
    # Test navigation
    print(browser.get_current())
    print(browser.back())
    print(browser.back())
    print(browser.forward())
    
    # Visit a new page (should clear forward history)
    print(browser.visit("https://www.example.com/page3"))
    print(browser.get_current())
    
    # Try to go forward (should have no forward history)
    print(browser.forward())
    
    # Test edge cases
    print(browser.back())
    print(browser.back())
    print(browser.back())  # Should show no back history
    
    print("All browser history tests completed successfully!")
if __name__ == "__main__":
    test_browser_history()

