with open('style.css', 'a') as f:
    f.write('''\n
/* 3 Video Swap Animations */
@keyframes videoSwap3_1 {
  0%, 33.32% { opacity: 1; }
  33.33%, 100% { opacity: 0; }
}
@keyframes videoSwap3_2 {
  0%, 33.32% { opacity: 0; }
  33.33%, 66.65% { opacity: 1; }
  66.66%, 100% { opacity: 0; }
}
@keyframes videoSwap3_3 {
  0%, 66.65% { opacity: 0; }
  66.66%, 100% { opacity: 1; }
}
''')
print("Appended keyframes.")
