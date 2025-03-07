document.addEventListener('DOMContentLoaded', function() {
  // Fade-in animation for elements with the 'fade-in' class
  const fadeElements = document.querySelectorAll('.fade-in');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.1 });
  
  fadeElements.forEach(element => {
    observer.observe(element);
  });
  
  // Add parallax effect to header images
  const parallaxElements = document.querySelectorAll('.parallax-bg');
  
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    
    parallaxElements.forEach(element => {
      const speed = element.dataset.speed || 0.5;
      element.style.transform = `translateY(${scrollY * speed}px)`;
    });
  });
  
  // Initialize tooltips
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
});