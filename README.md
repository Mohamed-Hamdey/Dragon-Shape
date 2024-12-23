# Dragon Shape

This project is a visualization of a dragon shape using OpenGL. It demonstrates the use of 2D graphics rendering techniques and transformations in OpenGL to create a complex geometrical figure based on a set of coordinates.

## Features
- **2D Rendering**: The dragon shape is rendered in a 2D space using OpenGL.
- **Coordinate System**: The shape is built using a predefined set of coordinates.
- **Customizable**: Users can modify the coordinates to adjust the shape as needed.
- **Scalable**: The code is structured to be extended for other shapes or transformations.
- 
## Images
### Origin
![Alt text](https://github.com/Mohamed-Hamdey/Dragon-Shape/blob/main/Origin.jpeg)
### White 
![Alt text](https://github.com/Mohamed-Hamdey/Dragon-Shape/blob/main/Light.png)
### Black
![Alt text](https://github.com/Mohamed-Hamdey/Dragon-Shape/blob/main/Dark.png)
### colored
![Alt text](https://github.com/Mohamed-Hamdey/Dragon-Shape/blob/main/colored.png)


## Prerequisites
To run this project, you need to have the following installed on your system:

- A C++ compiler (e.g., GCC, Clang, or MSVC)
- OpenGL library
- GLUT (OpenGL Utility Toolkit)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Mohamed-Hamdey/Dragon-Shape.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Dragon-Shape
   ```

3. Make sure you have OpenGL and GLUT installed on your system. On Ubuntu, you can install them using:
   ```bash
   sudo apt-get install freeglut3-dev
   ```

   On Windows, you may need to download and configure GLUT manually.

4. Compile the code using your preferred C++ compiler. For example:
   ```bash
   g++ dragon.cpp -o dragon -lGL -lGLU -lglut
   ```

## Usage

1. Run the compiled executable:
   ```bash
   ./dragon
   ```

2. The OpenGL window will open, displaying the dragon shape.

## Code Overview

The main source file is `dragon.cpp`, which contains the following key sections:

1. **Coordinate Data**: A dictionary or array that defines the points used to construct the dragon shape.
2. **OpenGL Initialization**: Code to set up the OpenGL rendering environment.
3. **Drawing Function**: The function that uses the coordinates to render the dragon shape on the screen.
4. **Main Loop**: The entry point of the application that initializes GLUT and starts the rendering loop.

## Example Coordinate System
The dragon shape is constructed using the following sample coordinates:

```cpp
std::map<std::string, std::pair<float, float>> coordinates = {
    {"C", {-7.4267149910554, -0.5238883440408}},
    {"D", {-6.2721363560766, 1.3811664036743}},
    {"E", {-4.3670816083615, 5.9994809435897}},
    // ... (Add other coordinates here)
};
```

These points are connected to form the desired dragon shape.

## Contributing

Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the OpenGL community for extensive documentation and tutorials.
- Inspired by geometric rendering techniques in computer graphics.