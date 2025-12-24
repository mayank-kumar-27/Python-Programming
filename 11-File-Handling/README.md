# File Handling

## Theory
File handling is the process of reading from and writing to files on the disk. Python provides built-in functions and methods to work with files. Files are opened using the open() function, which returns a file object. Files can be opened in different modes like read ('r'), write ('w'), append ('a'), etc. It's important to close files after use to free up system resources. The 'with' statement provides a convenient way to handle files as it automatically closes the file when done.

## Objective
The objective of this section is to learn how to perform file operations in Python. By the end of this section, you should be able to:
- Open and close files properly
- Read from files using different methods
- Write to files and append data
- Work with binary files
- Perform file and directory operations
- Use pathlib for modern path handling
- Handle temporary files and context managers

## Files
1. **01_file_basics.py** - Basic file creation and writing
2. **02_open_function.py** - Using the open() function
3. **03_file_modes.py** - Different file opening modes
4. **04_reading_files_read.py** - Reading entire file content
5. **05_reading_files_readline.py** - Reading one line at a time
6. **06_reading_files_readlines.py** - Reading all lines into a list
7. **07_writing_files.py** - Writing text to files
8. **08_appending_files.py** - Appending data to existing files
9. **09_with_statement.py** - Using with statement for file handling
10. **10_file_methods.py** - File object methods and properties
11. **11_file_tell_seek.py** - File pointer positioning
12. **12_file_truncate.py** - Truncating file content
13. **13_file_iteration.py** - Iterating over file lines
14. **14_binary_files.py** - Working with binary files
15. **15_reading_binary.py** - Reading binary data
16. **16_writing_binary.py** - Writing binary data
17. **17_file_exists_check.py** - Checking if file exists
18. **18_file_copy.py** - Copying files
19. **19_file_rename.py** - Renaming files
20. **20_file_delete.py** - Deleting files
21. **21_directory_operations.py** - Basic directory operations
22. **22_list_directory.py** - Listing directory contents
23. **23_create_directory.py** - Creating directories
24. **24_remove_directory.py** - Removing directories
25. **25_walk_directory.py** - Walking through directory trees
26. **26_path_operations.py** - Path manipulation operations
27. **27_pathlib_basics.py** - Using pathlib module
28. **28_file_properties.py** - Getting file properties
29. **29_temporary_files.py** - Working with temporary files
30. **30_context_managers_files.py** - Custom context managers for files

## Conclusion
File handling is essential for data persistence and manipulation in Python programs. This section has covered comprehensive file operations from basic read/write to advanced directory management and modern pathlib usage. Always remember to handle files properly using the 'with' statement to ensure they are closed automatically. Practice these operations with different file types and scenarios to become proficient in file handling.