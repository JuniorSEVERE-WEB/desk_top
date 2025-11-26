lst = [1, 2, 3]
print(id(lst))

lst.append(4)  # modifies in-place
print(id(lst))
