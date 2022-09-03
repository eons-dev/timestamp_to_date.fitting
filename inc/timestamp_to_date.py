import os
import logging
from datetime import datetime
from pipeadapter import Fitting

class timestamp_to_date(Fitting):
    def __init__(this, name="Timestamp to Date"):
        super().__init__(name)

        this.requiredKWArgs.append("timestamp")

        this.optionalKWArgs["output_format"] = '%m/%d/%Y'

    # Required Fitting method. See that class for details.
    def Run(this):
        dt = datetime.fromtimestamp(this.timestamp)
        this.output["date"] = dt.strftime(this.output_format)