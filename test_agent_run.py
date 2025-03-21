import asyncio
import logging
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import necessary functions from webui.py and default config
from webui import run_with_stream
from src.utils.default_config_settings import default_config

async def test_agent_run():
    # Get default configuration
    test_params = default_config()

    logger.info("🚦 Starting test run with parameters:")
    logger.info(f"  Agent Type: {test_params['agent_type']}")
    logger.info(f"  LLM Provider: {test_params['llm_provider']}")
    logger.info(f"  LLM Model: {test_params['llm_model_name']}")
    logger.info(f"  Task: {test_params['task']}")

    try:
        # Convert dictionary to positional arguments matching run_with_stream's signature
        args = [
            test_params['agent_type'],
            test_params['llm_provider'],
            test_params['llm_model_name'],
            test_params['llm_num_ctx'],
            test_params['llm_temperature'],
            test_params['llm_base_url'],
            test_params['llm_api_key'],
            test_params['use_own_browser'],
            test_params['keep_browser_open'],
            test_params['headless'],
            test_params['disable_security'],
            test_params['window_w'],
            test_params['window_h'],
            test_params['save_recording_path'],
            test_params['save_agent_history_path'],
            test_params['save_trace_path'],
            test_params['enable_recording'],
            test_params['task'],
            '',  # add_infos is empty by default
            test_params['max_steps'],
            test_params['use_vision'],
            test_params['max_actions_per_step'],
            test_params['tool_calling_method'],
            '',  # chrome_cdp is empty by default
            32000  # max_input_tokens default
        ]

        async for result in run_with_stream(*args):
            # Log each result from the stream
            logger.info("Received result from stream:")
            logger.info(f"Browser View HTML Length: {len(result[0]) if result[0] else 0}")
            logger.info(f"Final Result: {result[1]}")
            logger.info(f"Errors: {result[2]}")
            logger.info(f"Model Actions: {result[3]}")
            logger.info(f"Model Thoughts: {result[4]}")
            logger.info(f"Recording GIF: {'Present' if result[5] else 'None'}")
            logger.info(f"Trace File: {'Present' if result[6] else 'None'}")
            logger.info(f"Agent History File: {'Present' if result[7] else 'None'}")
            logger.info("---")

    except Exception as e:
        logger.error(f"Error during test run: {str(e)}", exc_info=True)

if __name__ == "__main__":
    # Run the async test
    asyncio.run(test_agent_run()) 