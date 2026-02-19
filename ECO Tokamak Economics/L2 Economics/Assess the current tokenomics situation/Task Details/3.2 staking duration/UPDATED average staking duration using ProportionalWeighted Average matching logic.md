The fundamental difference from the simpler FIFO model is that this script maintains a dynamic list of active_stakes for each depositor. Each entry in this list represents a past Deposited event and tracks two key pieces of information:

- time: The timestamp of the original deposit.
- amount: The remaining amount of that original deposit that is still considered "staked."

Matching logic: **Proportional/Weighted Average, **where each unstake event is treated as a partial withdrawal from all active stakes, proportional to their amount. This assumes all staked funds are pooled together and withdrawn uniformly. 

Histogram

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d7bb79df-1c80-41f9-a5b4-cf51ee823142/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7XP32KI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdkE444C4OeI0xV5KGWESVJx80KJG9nezxHgmU1K901gIhAPWr7Ti%2FUxEWE3m60Nfmo%2BpRjqhsGC490wWMoI%2Bs%2B3BFKv8DCHQQABoMNjM3NDIzMTgzODA1IgzXxBXeSXE0eWDybXMq3AMFtrob%2FpiXZAzfnzBVAnWUERCPkqe75AFuLWeRsRTdDyKKUaUKSI5lvBe9UNCNzZGLq%2FZo3k2xnXxnkD8QhhS1y2oSDuif%2BuGiimDk2M9%2FjySjO0CxqMbYSVoGfR0IksfvegN8c%2BcesXBenzjSrxywzk0cgPulPuAMKc8gK%2B3JqnGGbKFOz1HqGmFRQphjrhoKnNq%2BhbMTm7%2B%2BVrlgF7LvLkMGF9OEncgF9KSU%2BjZ1s7zYzeRT78%2F76MIDCoivHanEfot7ClMlvceQJRRIr7b9WcYbHQdSLYIFDkarqIzAxYe%2FSwrrE%2F%2BjPnjndD3G9VFTaC%2BvuyQInk6Qf4lnfjI62jWCUZzz5JE%2BvNDde6dZcCoITp0WR%2FErdCMp0R3NGTqR37G4eJHBZi2KFJcCITNBAVoN6limRvHJ2j9xXn%2FOF77QwZFfK3Qfo9TKjl%2FrfiOfUoGvFgIC9xjXsT71GTb%2Bib3YpTDefk9UuoqXaEnW1Z7o6g0oNbI3ziO4JG4vrG7iY0fIpTwy4kfdeheL7MHyp1FQjt0ib3HfXrmmO9en1qM6J5jODoLSNt89S%2Brx6WwRNX57VzszKw0jFFxOW719P4hLUSpgGtXwF%2BAq%2FSKWaUBl6z2zFeKSb0HQ1TDE79nMBjqkAfPd40kG94iNuwXlH3dh9vVhP9RCLaM6VmCVTXQYX%2Ba3s6P2jJIT69tD9%2FojVmu6gNMvXv37eKdijRThkqa0RvnF3GRYbdRAc1Se60qmcIkLwLRo%2B4Bwuzb4J5nQ2qGtDa0TlT5yIEpvRQplTWA5FY2Pe06jJetcFmBZexDYRfn1MoHMuh3FE0WqXMGp8Z6B68hWXyQQ2uGRXDCwyyvzkbeRcv0I&X-Amz-Signature=df9c45bc5d8e0907e30ae6d21adc4e1de7bd5322eff8d2d1e73276a0c397399b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Boxplot

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/00078988-63d4-43a4-85a8-08128c46ff38/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7XP32KI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdkE444C4OeI0xV5KGWESVJx80KJG9nezxHgmU1K901gIhAPWr7Ti%2FUxEWE3m60Nfmo%2BpRjqhsGC490wWMoI%2Bs%2B3BFKv8DCHQQABoMNjM3NDIzMTgzODA1IgzXxBXeSXE0eWDybXMq3AMFtrob%2FpiXZAzfnzBVAnWUERCPkqe75AFuLWeRsRTdDyKKUaUKSI5lvBe9UNCNzZGLq%2FZo3k2xnXxnkD8QhhS1y2oSDuif%2BuGiimDk2M9%2FjySjO0CxqMbYSVoGfR0IksfvegN8c%2BcesXBenzjSrxywzk0cgPulPuAMKc8gK%2B3JqnGGbKFOz1HqGmFRQphjrhoKnNq%2BhbMTm7%2B%2BVrlgF7LvLkMGF9OEncgF9KSU%2BjZ1s7zYzeRT78%2F76MIDCoivHanEfot7ClMlvceQJRRIr7b9WcYbHQdSLYIFDkarqIzAxYe%2FSwrrE%2F%2BjPnjndD3G9VFTaC%2BvuyQInk6Qf4lnfjI62jWCUZzz5JE%2BvNDde6dZcCoITp0WR%2FErdCMp0R3NGTqR37G4eJHBZi2KFJcCITNBAVoN6limRvHJ2j9xXn%2FOF77QwZFfK3Qfo9TKjl%2FrfiOfUoGvFgIC9xjXsT71GTb%2Bib3YpTDefk9UuoqXaEnW1Z7o6g0oNbI3ziO4JG4vrG7iY0fIpTwy4kfdeheL7MHyp1FQjt0ib3HfXrmmO9en1qM6J5jODoLSNt89S%2Brx6WwRNX57VzszKw0jFFxOW719P4hLUSpgGtXwF%2BAq%2FSKWaUBl6z2zFeKSb0HQ1TDE79nMBjqkAfPd40kG94iNuwXlH3dh9vVhP9RCLaM6VmCVTXQYX%2Ba3s6P2jJIT69tD9%2FojVmu6gNMvXv37eKdijRThkqa0RvnF3GRYbdRAc1Se60qmcIkLwLRo%2B4Bwuzb4J5nQ2qGtDa0TlT5yIEpvRQplTWA5FY2Pe06jJetcFmBZexDYRfn1MoHMuh3FE0WqXMGp8Z6B68hWXyQQ2uGRXDCwyyvzkbeRcv0I&X-Amz-Signature=ad74e359c8782aeeba877bca2a3b626ee4adf2aaba8d3b426aba78db1ec2be32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```python
import pandas as pd
from datetime import timedelta
import numpy as np

def calculate_proportional_weighted_average(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Convert Timestamp to datetime objects
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Convert Amount to numeric
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df.dropna(subset=['Amount'], inplace=True)

    # Filter for relevant event types and sort by timestamp
    df_events = df[df['EventType'].isin(['Deposited', 'Unstaking'])].sort_values(by='Timestamp')

    # Group by the staker's address (Depositor)
    grouped = df_events.groupby('Depositor')

    total_weighted_duration = 0.0 # Sum of (duration_seconds * amount)
    total_amount_unstaked = 0.0
    total_cycles = 0

    # Iterate over each staker
    for depositor, events in grouped:
        # List of active stakes: [(stake_time, stake_amount)]
        active_stakes = []
        
        for index, row in events.iterrows():
            amount = row['Amount']
            timestamp = row['Timestamp']
            
            if row['EventType'] == 'Deposited':
                # Add new stake to the list
                active_stakes.append({'time': timestamp, 'amount': amount})
            
            elif row['EventType'] == 'Unstaking':
                unstake_amount = amount
                
                # Calculate the total amount currently staked
                total_active_amount = sum(s['amount'] for s in active_stakes)
                
                if total_active_amount == 0:
                    # This unstake is not covered by any recorded stake, skip it
                    continue

                # The unstake is applied proportionally to all active stakes
                for stake in active_stakes:
                    # Calculate the proportion of this unstake that comes from the current active stake
                    proportion = stake['amount'] / total_active_amount
                    unstake_from_this_stake = unstake_amount * proportion
                    
                    if unstake_from_this_stake > 0:
                        duration = timestamp - stake['time']
                        
                        # Weighted duration contribution: (duration_seconds * amount_unstaked_from_this_stake)
                        total_weighted_duration += duration.total_seconds() * unstake_from_this_stake
                        total_amount_unstaked += unstake_from_this_stake
                        total_cycles += 1 # Counting each proportional withdrawal as a cycle for tracking

                # Update the active stakes list by reducing their amount
                # This is the crucial step for the proportional model
                for stake in active_stakes:
                    proportion = stake['amount'] / total_active_amount
                    stake['amount'] -= unstake_amount * proportion
                
                # Remove any stakes that have been fully withdrawn (amount <= 0)
                active_stakes = [s for s in active_stakes if s['amount'] > 0]


    if total_amount_unstaked == 0:
        return "No complete staking cycles (Deposited followed by Unstaking) found in the data."

    # Calculate the final weighted average duration in seconds
    weighted_average_seconds = total_weighted_duration / total_amount_unstaked
    
    # Convert the weighted average seconds back to a timedelta object
    weighted_average_duration = timedelta(seconds=weighted_average_seconds)

    # Convert the average duration to a human-readable format
    total_seconds = weighted_average_duration.total_seconds()
    days = int(total_seconds // (24 * 3600))
    hours = int((total_seconds % (24 * 3600)) // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return {
        "weighted_average_duration_timedelta": weighted_average_duration,
        "weighted_average_duration_human_readable": f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds",
        "total_amount_unstaked": total_amount_unstaked
    }

if __name__ == "__main__":
    file_path = '/home/ubuntu/upload/10837675_18231453.csv'
    result = calculate_proportional_weighted_average(file_path)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"Total amount unstaked (smallest unit): {result['total_amount_unstaked']:.0f}")
        print(f"Weighted average staking time (timedelta): {result['weighted_average_duration_timedelta']}")
        print(f"Weighted average staking time: {result['weighted_average_duration_human_readable']}")
```

Histogram:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_histogram(data_file, output_file):
    # Load the staking durations in seconds
    df = pd.read_csv(data_file)
    
    # Convert duration from seconds to days for better visualization
    df['duration_days'] = df['duration_seconds'] / (24 * 3600)
    
    # The true weighted average is 121 days, 3 hours, 29 minutes, and 47 seconds.
    # 121 + (3/24) + (29/1440) + (47/86400) = 121.145771759 days
    TRUE_WEIGHTED_AVERAGE_DAYS = 121.15

    # Set up the plot
    plt.figure(figsize=(12, 6))
    
    # Create the histogram
    # Use a number of bins that is appropriate for the data range.
    n_bins = int(np.sqrt(len(df)))
    
    plt.hist(df['duration_days'], bins=n_bins, color='lightcoral', edgecolor='darkred', alpha=0.7)
    
    # Add a vertical line for the true weighted average staking time
    plt.axvline(TRUE_WEIGHTED_AVERAGE_DAYS, color='darkred', linestyle='dashed', linewidth=1.5, 
                label=f'Weighted Average: {TRUE_WEIGHTED_AVERAGE_DAYS:.2f} days')

    # Add labels and title
    plt.title('Distribution of Staking Times (Proportional Matching)', fontsize=16)
    plt.xlabel('Staking Duration (Days)', fontsize=12)
    plt.ylabel('Frequency (Number of Proportional Withdrawals)', fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    
    # Save the plot
    plt.savefig(output_file)
    plt.close()
    
    print(f"Histogram saved to {output_file}")

if __name__ == "__main__":
    data_file = 'proportional_durations_seconds.csv'
    output_file = 'proportional_staking_time_histogram_corrected.png'
    create_histogram(data_file, output_file)
```

Boxplot:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_boxplot(data_file, output_file):
    # Load the staking durations in seconds
    df = pd.read_csv(data_file)
    
    # Convert duration from seconds to days for better visualization
    df['duration_days'] = df['duration_seconds'] / (24 * 3600)
    
    # Set up the plot
    plt.figure(figsize=(10, 6))
    
    # Create the box plot
    plt.boxplot(df['duration_days'], vert=False, patch_artist=True, 
                boxprops=dict(facecolor='lightcoral'),
                medianprops=dict(color='darkred', linewidth=2))
    
    # Add labels and title
    plt.title('Box Plot of Staking Times (Proportional Matching)', fontsize=16)
    plt.xlabel('Staking Duration (Days)', fontsize=12)
    plt.yticks([1], ['Staking Time'])
    
    # Add text for key statistics
    median = df['duration_days'].median()
    q1 = df['duration_days'].quantile(0.25)
    q3 = df['duration_days'].quantile(0.75)
    
    plt.text(median, 1.1, f'Median: {median:.2f} days', ha='center', color='darkred', weight='bold')
    plt.text(q1, 1.05, f'Q1: {q1:.2f} days', ha='center')
    plt.text(q3, 1.05, f'Q3: {q3:.2f} days', ha='center')

    # Adjust layout to prevent labels from being cut off
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(output_file)
    plt.close()
    
    print(f"Box plot saved to {output_file}")

if __name__ == "__main__":
    data_file = 'proportional_durations_seconds.csv'
    output_file = 'proportional_staking_time_boxplot.png'
    create_boxplot(data_file, output_file)
```