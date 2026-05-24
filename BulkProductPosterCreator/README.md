# Poster Maker

A powerful desktop application for creating professional product posters by overlaying product images onto customizable templates.

![Poster Maker Screenshot](screenshot.png)

## Project Overview

Poster Maker is a specialized desktop application designed for e-commerce professionals, marketers, and designers who need to quickly generate high-quality product posters. Unlike general-purpose photo editors, Poster Maker focuses specifically on the workflow of placing product images onto pre-designed templates with precise positioning, scaling, and batch generation capabilities.

The application enables users to:
- Load multiple template backgrounds (PNG/JPG)
- Import folders of product images
- Precisely position and scale products on templates using drag-and-drop, keyboard nudging, and zoom controls
- Save positioning presets for consistent branding across different templates
- Generate single posters or batch process entire product catalogs
- Create professional marketing materials in minutes instead of hours

## Installation Guide

### Prerequisites
- Python 3.7 or higher
- Windows, macOS, or Linux operating system

### Installation Steps

1. **Install Python dependencies:**
   ```bash
   pip install pillow
   ```

2. **Run the application directly:**
   ```bash
   python Final.py
   ```

3. **Optional - Icon conversion utility:**
   The `png_to_ico.py` script can convert PNG icons to Windows ICO format:
   ```bash
   python png_to_ico.py app_icon.png
   ```

### Alternative: Pre-built Executable
The application is also available as a standalone executable in the `dist/` directory (`Final.exe`). Simply download and run without requiring Python installation.

## Usage Instructions

### Getting Started
1. Launch the application: `python Final.py` or run `Final.exe`
2. The interface is divided into three main sections:
   - **Left panel**: Template and product image lists
   - **Center canvas**: Visual preview of template with positioned product
   - **Right panel**: Controls for positioning, zoom, and generation

### Template Management
- **Add Templates**: Click "Add Template" button to select one or more template images (PNG/JPG)
- **Select Template**: Click on a template in the list to load it
- **Template Presets**: Save default positioning for a template using "Save Template Preset"

### Product Image Management
- **Load Product Folder**: Click "Load Product Folder" to import all PNG/JPG images from a directory
- **Navigate Products**: Use "Prev"/"Next" buttons or click items in the product list
- **Remove Products**: Select items and click "Remove (X)"; use "Undo Delete" to restore

### Positioning and Scaling Controls
- **Drag & Drop**: Click and drag the product image on the canvas for intuitive positioning
- **Keyboard Nudging**: With canvas focused, use arrow keys for pixel-perfect adjustments (2px steps by default)
- **Zoom Controls**: "+"/"-" keys or "Zoom +"/"Zoom -" buttons to zoom canvas for detailed work
- **Mouse Wheel**: Scroll to zoom in/out
- **Position Reset**: Double-click canvas or use "Reposition" button to reset to template center

### Saving and Loading Positions
- **Save Current Position**: Click "Save Product Pos" to save the current product's position for the selected template
- **Copy Position**: Use "Copy Pos To Selected Templates" to apply current position to other templates
- **Reposition from Previous**: "Reposition (from prev template)" automatically scales positions when switching between templates of different sizes
- **Presets File**: All positions are saved to `presets.json` in the application directory

### Generation Options
- **Generate All**: Creates posters for all loaded products on the currently selected template
- **Generate All (all templates)**: Creates posters for all products on all templates
- **Output Format**: Choose between PNG (lossless) or JPG (smaller file size) via the format dropdown
- **Output Folder**: Specify custom output directory via "Output Folder" button

### Advanced Features
- **Copy & Reposition All**: Copy current template's positions to all other templates with automatic scaling
- **Batch Processing**: Generate hundreds of posters with a single click
- **Undo System**: Comprehensive undo for product removal operations
- **Error Logging**: Detailed error logs in `error.log` for troubleshooting

## GitHub Guidelines

### Repository Setup
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m pytest tests/`

### Branching Strategy
- `main`: Production-ready releases
- `develop`: Active development branch
- Feature branches: `feature/<feature-name>` for new functionality
- Release branches: `release/v<major>.<minor>` for release preparation
- Hotfix branches: `hotfix/<issue>` for critical production fixes

### Commit Message Conventions
Follow conventional commit format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
**Scopes:** `gui`, `image-processing`, `build`, `utility`, `error-handling`

Example: `feat(gui): add template preview thumbnails`

### Pull Request Workflow
1. Create feature branch from `develop`
2. Implement changes with proper testing
3. Push branch and create PR to `develop`
4. Include description of changes, screenshots, and testing results
5. Address review comments
6. Merge after approval

### Contribution Guidelines
- Follow PEP 8 coding standards
- Add documentation for new features
- Write unit tests for new functionality
- Update README.md for significant changes
- Maintain backward compatibility when possible

### Issue Reporting
When reporting issues, please include:
- Application version (check `Final.py` header)
- OS and Python version
- Steps to reproduce
- Expected vs. actual behavior
- Relevant error messages from `error.log`
- Screenshots if applicable

## Technical Documentation

### Architecture Overview
Poster Maker follows a modular architecture with clear separation of concerns:
- **GUI Layer**: Tkinter-based interface with Canvas for visual rendering
- **Business Logic**: Position management, template/product handling, preset persistence
- **Image Processing**: PIL/Pillow for image manipulation and compositing
- **Persistence Layer**: JSON-based preset storage

### Core Components

#### GUI Interface
- Built with Tkinter using a responsive layout
- Canvas widget for template visualization and interactive positioning
- Listboxes for template and product management
- Status bar showing real-time information about current state

#### Canvas Functionality
- Real-time rendering of templates with positioned products
- Drag-and-drop interaction for intuitive positioning
- Keyboard nudge system with configurable step size
- Zoom functionality with mouse wheel and keyboard shortcuts
- Bounding box visualization for precise alignment

#### Image Processing Features
- Multi-resolution scaling with Lanczos resampling
- Alpha channel preservation for transparent overlays
- Template-product compositing with alpha blending
- Automatic aspect ratio preservation during scaling
- Error handling for corrupted or unreadable images

#### Persistence System
- JSON-based preset storage in `presets.json`
- Debounced saving to prevent excessive disk I/O
- Template-specific positioning data structure
- Per-product and template-default position storage
- Automatic backup of corrupt JSON files

### Error Handling
- Comprehensive exception handling throughout the application
- Detailed error logging to `error.log` with timestamps
- User-friendly error messages via messagebox dialogs
- Graceful degradation when components fail
- Automatic recovery from common issues like missing files

## File Structure Explanation

```
PosterMaker/
├── Final.py                # Main application code (Tkinter GUI + business logic)
├── png_to_ico.py           # Utility script for PNG to ICO conversion
├── Final.spec              # PyInstaller build configuration
├── presets.json            # Saved positioning presets (auto-generated)
├── error.log               # Application error log (auto-generated)
├── app_icon.ico            # Windows application icon
├── app_icon.png            # Application icon source (PNG format)
├── build/                  # PyInstaller build artifacts
│   └── Final/              # Build output directory
├── dist/                   # Distributable executables
│   └── Final.exe           # Standalone Windows executable
└── README.md               # This documentation file
```

### Key Files Details

- **`Final.py`**: The core application containing the `PosterMakerApp` class, GUI construction, event handlers, and image processing logic. Implements all user-facing functionality.

- **`png_to_ico.py`**: A utility script that converts PNG images to multi-resolution ICO files suitable for Windows applications, using PIL's ICO format support.

- **`Final.spec`**: PyInstaller configuration file that specifies build options including the application icon (`app_icon.ico`) and packaging settings.

- **`presets.json`**: JSON file that stores all saved positioning data. Contains template-specific entries with both default positions and per-product positions.

- **`error.log`**: Log file that captures detailed error information including stack traces and timestamps for debugging purposes.

## Build Process

### Creating Distributable Executables
Poster Maker uses PyInstaller to create standalone executables:

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable:**
   ```bash
   pyinstaller Final.spec
   ```

3. **Locate the executable:**
   The built executable will be in the `dist/` directory as `Final.exe`

### PyInstaller Configuration Details
- **Icon Integration**: The `Final.spec` file specifies `icon=['app_icon.ico']` to embed the application icon
- **Console Mode**: `console=False` creates a windowed application without console window
- **UPX Compression**: Enabled for smaller executable size
- **Data Files**: No additional data files required beyond the main script

### Customizing the Build
To modify build options, edit the `Final.spec` file:
- Change `name='Final'` to customize the executable name
- Modify `upx=True` to disable compression for faster builds
- Adjust `icon` parameter to use a different icon file
- Change `console=False` to `console=True` for debugging with console output

## Troubleshooting

### Common Issues and Solutions

#### Missing Pillow Dependency
**Symptom**: ImportError when launching the application
**Solution**: Install Pillow dependency
```bash
pip install pillow
```

#### Unreadable Image Files
**Symptom**: Warning messages about unreadable templates or products
**Causes**: Corrupted files, unsupported formats, permission issues
**Solutions**: 
- Verify files are valid PNG/JPG images
- Check file permissions
- Try opening images in another application

#### Template Size Issues
**Symptom**: Incorrect positioning when switching between templates of different sizes
**Solution**: Use "Reposition (from prev template)" or "Copy & Reposition All" which automatically calculates scaling ratios

#### Preset Loading Problems
**Symptom**: Positions not loading correctly or `presets.json` corruption
**Solutions**: 
- Check `error.log` for JSON parsing errors
- Look for `.corrupt.*` backup files in the application directory
- Manually edit `presets.json` to fix syntax errors

#### Performance Issues with Large Images
**Symptom**: Slow rendering or unresponsive UI
**Solutions**: 
- Use smaller template images (under 2000x2000 pixels)
- Close unused applications to free memory
- Increase system virtual memory if needed

#### Build Failures
**Symptom**: PyInstaller build errors
**Solutions**: 
- Ensure all dependencies are installed
- Check `warn-Final.txt` in the build directory for warnings
- Verify `app_icon.ico` exists in the project root
- Try cleaning build artifacts: `pyinstaller --clean Final.spec`

### Debugging Tips
- Enable console mode by changing `console=False` to `console=True` in `Final.spec`
- Check `error.log` for detailed error information
- Use the status bar at the bottom of the application for real-time feedback
- Test with sample images before processing large batches

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PIL/Pillow for powerful image processing capabilities
- Tkinter for cross-platform GUI development
- PyInstaller for creating standalone executables
- The open-source community for inspiration and best practices

## Contact

For questions, suggestions, or bug reports, please contact the maintainers or open an issue on GitHub.