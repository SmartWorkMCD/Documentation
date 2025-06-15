# Coral CameraThing Project

This project utilizes OpenCV to open the camera and continuously capture frames in a loop. The captured frames can be processed or displayed as needed.

## Project Structure

```
coral
└── camerathing
    ├── src
    │   ├── main.py
    ├── Dockerfile
    ├── requirements.txt
    └── README.md
```

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Clone the repository or download the project files.
2. Navigate to the `camerathing` directory.

## Setup

To set up the project, create a virtual environment and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, you can either execute the Python script directly or build and run the Docker container.

### Running Directly

Run the following command:

```bash
python src/main.py
```

### Running with Docker

1. Build the Docker image:

```bash
docker build -t camerathing .
```

2. Run the Docker container:

```bash
docker run --device=/dev/video0 -it camerathing
```

Make sure to replace `/dev/video0` with the appropriate device path for your camera if necessary.

## License

This project is licensed under the MIT License.