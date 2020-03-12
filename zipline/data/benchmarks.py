#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pandas as pd
import requests


def get_benchmark_returns(symbol):
    
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    df = pd.read_csv("/data/" + symbol + ".csv", parse_dates=['Date'], date_parser=dateparse)

    df.index = pd.DatetimeIndex(df['Date'])
    df = df['Close']

    return df.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
