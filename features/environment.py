from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    
# Hook to run after all tests (teardown)
def after_all(context):
    print("Tearing down environment")
    context.driver.quit()

# Hook to run before each scenario
def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    context.driver.get("http:google.com")
    


# Hook to run after each scenario
def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name}")

# Hook to run before each step
def before_step(context, step):
    print(f"Starting step: {step.name}")

# Hook to run after each step
def after_step(context, step):
    if step.status == "failed":
        print(f"Step failed: {step.name}")
        take_screenshot(context, step)
    print(f"Finished step: {step.name}")
    take_screenshot(context, step)





def take_screenshot(context, step):
    # Ensure there's a directory for screenshots
    screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Generate a unique file name based on the scenario and step name
    file_name = f"{step}.png".replace(" ", "_").replace("/", "_")
    file_path = os.path.join(screenshots_dir, file_name)

    # Capture the screenshot and save it
    context.driver.save_screenshot(file_path)
    print(f"Screenshot saved to: {file_path}")