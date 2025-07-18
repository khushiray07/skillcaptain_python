function highlightElements() {

    document.querySelectorAll('.highlighted').forEach(el => {
    el.classList.remove('highlighted');
  });

  const selector = document.getElementById('selectorInput').value;

  try {

    const elements = document.querySelectorAll(selector);

    if (elements.length === 0) {
      alert("No elements matched the selector.");
    }

    elements.forEach(el => el.classList.add('highlighted'));
  } catch (error) {
    alert("Invalid CSS selector.");
  }
}
