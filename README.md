{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true,
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import psycopg2\n",
    "import psycopg2.extras as extras"
   ]
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Reading the Dataset"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"~/Downloads/all_races.csv\",sep=\",\", low_memory=False)"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Preprossesing and Cleaning the data"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "outputs": [
    {
     "data": {
      "text/plain": "         place age_class place_in_class     bib         name     sex  nation  \\\ncount   293858    293848         293858  293858       293858  293858  293858   \nunique   10880        41           2730   14207        39969       2     106   \ntop        992       M20              1     504  Pedro Silva       M      PT   \nfreq        76     70254            816      60          580  236284  272970   \n\n              team              official_time                   net_time  \\\ncount       220530                     293858                     291706   \nunique       11222                      15050                      14868   \ntop     Individual  0 days 00:58:24.000000000  0 days 00:53:04.000000000   \nfreq         51210                        128                        152   \n\n        birth_date          event event_year distance  \ncount       293858         293858     293858   293858  \nunique       15192              7          7        5  \ntop     01/01/1992  sao-silvestre       2015       10  \nfreq           646          89838      66658   149534  ",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>place</th>\n      <th>age_class</th>\n      <th>place_in_class</th>\n      <th>bib</th>\n      <th>name</th>\n      <th>sex</th>\n      <th>nation</th>\n      <th>team</th>\n      <th>official_time</th>\n      <th>net_time</th>\n      <th>birth_date</th>\n      <th>event</th>\n      <th>event_year</th>\n      <th>distance</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>293858</td>\n      <td>293848</td>\n      <td>293858</td>\n      <td>293858</td>\n      <td>293858</td>\n      <td>293858</td>\n      <td>293858</td>\n      <td>220530</td>\n      <td>293858</td>\n      <td>291706</td>\n      <td>293858</td>\n      <td>293858</td>\n      <td>293858</td>\n      <td>293858</td>\n    </tr>\n    <tr>\n      <th>unique</th>\n      <td>10880</td>\n      <td>41</td>\n      <td>2730</td>\n      <td>14207</td>\n      <td>39969</td>\n      <td>2</td>\n      <td>106</td>\n      <td>11222</td>\n      <td>15050</td>\n      <td>14868</td>\n      <td>15192</td>\n      <td>7</td>\n      <td>7</td>\n      <td>5</td>\n    </tr>\n    <tr>\n      <th>top</th>\n      <td>992</td>\n      <td>M20</td>\n      <td>1</td>\n      <td>504</td>\n      <td>Pedro Silva</td>\n      <td>M</td>\n      <td>PT</td>\n      <td>Individual</td>\n      <td>0 days 00:58:24.000000000</td>\n      <td>0 days 00:53:04.000000000</td>\n      <td>01/01/1992</td>\n      <td>sao-silvestre</td>\n      <td>2015</td>\n      <td>10</td>\n    </tr>\n    <tr>\n      <th>freq</th>\n      <td>76</td>\n      <td>70254</td>\n      <td>816</td>\n      <td>60</td>\n      <td>580</td>\n      <td>236284</td>\n      <td>272970</td>\n      <td>51210</td>\n      <td>128</td>\n      <td>152</td>\n      <td>646</td>\n      <td>89838</td>\n      <td>66658</td>\n      <td>149534</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identify on the line 146929 an header duplicate in the middle of the dataset\n",
    "df = df.drop(axis=0, labels=146929)\n",
    "df.describe()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# of duplicates: 146935\n",
      "size of df: 293858\n"
     ]
    }
   ],
   "source": [
    "#counting duplicated\n",
    "print('# of duplicates:',len(df)-len(df.drop_duplicates()))\n",
    "print('size of df:',len(df))"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "outputs": [
    {
     "data": {
      "text/plain": "place             object\nage_class         object\nplace_in_class    object\nbib               object\nname              object\nsex               object\nnation            object\nteam              object\nofficial_time     object\nnet_time          object\nbirth_date        object\nevent             object\nevent_year        object\ndistance          object\ndtype: object"
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#removing the duplicates\n",
    "df = df.drop_duplicates()\n",
    "#writing file without duplicates\n",
    "df.to_csv('~/Downloads/all_races_no_duplicates.csv', index=False)\n",
    "#Checking the types of the colunms\n",
    "df.dtypes"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "outputs": [
    {
     "data": {
      "text/plain": "<Figure size 640x480 with 1 Axes>",
      "image/png": "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xJEBIonjyAAREVEFxpEBIioXjgwQSRtXExAREUkcpwmIiIgqME4TEFG5cJqASNo4TUBERCRxnCYgIiKqwDhNQETlwmkCImnjNAEREZHEcZqAiIioAivPNAFHBoiIiCSOPQNExJ4BIonjNAEREVEFxtUERFQuHBkgkjaODBAREVVgbCAkIiKiMnGagIg4TUAkcRwZICIikjj2DBAREVVgXE1AROXCaQIiaeM0ARERkcRxmoCIiKgC4zQBEZULpwmIpI0jA0RERBUYNx0iIiKiMnGagIg4TUAkcRwZICIikjj2DBAREVVgXE1AROXCaQIiaePIABERUQXG1QRERERUJoYBIiIiiWMYICIikjiGASIiIoljGCAiIpI4hgEiIiKJYxggIiKSOIYBIiIiiWMYICIikjhuR0xE3I6YSOK4HTEREVEFxu2IiYiIqEwMA0RERBLHMEBERCRxDANEREQSxzBAREQkcQwDREREEscwQEREJHHcdIiIuOkQkcRx0yEiIqIKjJsOERERUZk4TUBEnCYgkjhOExAREVVg5Zkm4MgAEXFkgEjiODJARERUgXFkgIjKhSMDRNLGkQEiIqIKjEsLiYiIqEwMA0RERBLHngEiYs8AkcSxZ4CIiKgC42oCIioXjgwQSRtHBoiIiCowjgwQUblwZIBI2riagIiISOI4TUBERFSBcdMhIiIiKhN7BoiIPQNEEseRASIiIoljGCAiIpI4hgEiIiKJ42oCIiKiCoyrCYiIiKhMDANEREQSx6WFRMSlhUQSx54BIiKiCow9A0RERFQmThMQEacJiCSOIwNEREQSx54BIiKiCow9A0RERFQm9gwQEXsGiCSO0wREREQVWHmmCTgyQEQcGSCSOPYMEBERSRynCYiIiCowriYgIiKiMjEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEaai6ACJSvXcpkaouQU6rQRdVl0AkORwZICIikjiZIAhCeR6ooWmo7FqIiIjoH5abnVzmYzhNQEScJiCSOE4TEBERSRzDABERkcSxZ4CIiKgCY88AEZULewaIpI0jA0RERBUYRwaIqFw4MkAkbRwZICIiqsA4MkBE5cKRASJp48gAERFRBVaekQHuM0BERCRxDANEREQSxzBAREQkcWwgJCI2EBJJHEcGiIiIJI5hgIiISOK4tJCIiKgC49JCIiIiKhPDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUmchqoLICJSZ+9SIlVdgpxWgy6qLoEqKJkgCEJ5HqihaajsWoiIiOgflpudXOZjOE1AREQkcQwDREREEscwQEREJHEMA0RERBLHMEBERCRxDANEREQSxzBAREQkcQwDREREEscwQEREJHEMA0RERBLHMEBERCRxDANEREQSxzBAREQkcQwDREREEscwQEREJHEMA0RERBKnoeoCiEj13qVEqroEOa0GXVRdApHkyARBEMrzQA1NQ2XXQkRERP+w3OzkMh/DaQIiIiKJYxggIiKSOIYBIiIiiWMYICIikjiGASIiIonj0kIi4tJCIonj0kIiIqIKjEsLiYiIqEycJiAiThMQSRxHBoiIiCSOPQNEREQVWHl6BjhNQEScJiCSOI4MEBERVWBcTUBERERlYhggIiKSOPYMEBF7Bogkjj0DREREFRh7BoiIiKhMDANEREQSx54BImLPAJHEcWSAiIhI4hgGiIiIJI6rCYiIiCowriYgIiKiMjEMEBERSRxXExARVxMQSRxHBoiIiCSODYREREQVGBsIiYiIqEwMA0RERBLHMEBERCRxDANEREQSxzBAREQkcQwDREREEscwQEREJHEMA0RERBLHMEBERCRxDANEREQSxzBAREQkcQwDREREEscwQEREJHEMA0RERBLHMEBERCRxDANEREQSxzBAREQkcQwDREREEscwQEREJHEMA0RERBLHMEBERCRxDANEREQSp6HqAohI9d6lRKq6BDmtBl1UXQKR5MgEQRDK80ANTUNl10JERET/sNzs5DIfw2kCIiIiiWMYICIikjiGASIiIoljGCAiIpI4hgEiIiKJYxggIiKSOIYBIiIiiWMYICIikjjuQEhE3IGQSOI4MkBERCRxDANEREQSxzBAREQkcTyoiIiIqALjQUVERERUJq4mICKuJiCSOI4MEBERSRzDABERkcQxDBAREUkcwwAREZHEcWkhERFRBcalhURERFQmhgEiIiKJYxggIiKSOIYBIiIiiWMYICIikjiGASIiIoljGCAiIpI4hgEiIiKJYxggIiKSOIYBIiIiiWMYICIikjiGASIiIoljGCAiIpI4hgEiIiKJYxggIiKSOIYBIiIiiWMYICIikjiGASIiIoljGCAiIpI4hgEiIiKJYxggIiKSOIYBIiIiiWMYICIikjiGASIiIoljGCAiIpI4DVUXQESq9y4lUtUlyGk16KLqEogkRyYIglCeB2poGiq7FiIiIvqH5WYnl/kYThMQERFJHMMAERGRxDEMEBERSRzDABERkcRxNQERcTUBkcRxNQEREVEFxtUEREREVCaGASIiIoljzwARsWeASOI4MkBERCRxbCAkIiKqwNhASERERGVizwARsWeASOI4TUBERFSBcZqAiIiIysQwQEREJHHsGSAi9gwQSRx7BoiIiCow9gwQERFRmRgGiIiIJI5hgIiISOIYBoiIiCSOYYCIiEjiGAaIiIgkjvsMEBH3GSCSOO4zQEREVIFxnwEiIiIqE6cJiIjTBEQSx5EBIiIiiWPPABERUQXGngEiIiIqE8MAERGRxDEMEBERSRzDABERkcRxaSERcWkhkcRxZICIiEjiuLSQiIioAuPSQiIiIioTwwAREZHEMQwQERFJHFcTEBFXExBJHBsIiYiIKjA2EBIREVGZGAaIiIgkjj0DRMSeASKJY88AERFRBcaeASIiIioTwwAREZHEsWeAiNgzQCRxHBkgIiKSODYQEhERVWDlaSDkNAERcZqASOI4MkBERFSBcWSAiMqFIwNE0sYGQiIiIonjNAEREVEFxh0IiYiIqEzsGSAi9gwQSRynCYiIiCowriYgonLhyACRtLFngIiISOI4TUBERFSBcTUBERERlYlhgIiISOIYBoiIiCSOYYCIiEjiGAaIiIgkjmGAiIhI4hgGiIiIJI5hgIiISOIYBoiIiCSOYYCIiEjieFAREfGgIiKJ49kEREREFRjPJiAiIqIyMQwQERFJHHsGiIg9A0QSx5EBIiIiiWMDIRERUQVWngZCThMQEacJiCSOIwNEREQVGJcWEhERUZk4TUBEnCYgkjhOExAREVVgnCYgIiKiMpV7ZICIiIgqJo4MEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAqbWMjAzk5+dDVUdoZGVlffJjf/zxh4iVENE/rbR/36om9mufKGEgLy8P58+fx/bt2/H69WvcunULb968EePWCjIzM7Fy5UokJCQgPz8fXl5eaNOmDYYNG4bk5LKPeFSG169f48OHDwCAe/fuISgoCNHR0Sqp5dChQxgyZAjatWuHjh07YsSIETh9+rTodQiCgI0bN8La2hodOnRAcnIyZsyYgfnz5yM7O1vUWpycnHD58mWFazk5OfjPf/6Dvn37iloLlS0uLg5TpkxB79698ezZM2zevBlHjx5VWT1PnjzBsmXL4O7ujufPn2Pfvn2IjY1VWT0PHjzAqVOnkJWVhSdPnqgkZNvZ2eHVq1fFrqempqJDhw6i1uLk5IT4+HhR71kaVb72KT0MPHv2DL169cLs2bOxYsUKZGRkICgoCA4ODvj999+VfXsFCxYswIULFyCTyXD48GFERETA398fenp6WLBggai1AMDp06fRtWtXxMXF4fHjxxg+fDgOHjwId3d3/Pzzz6LW8p///Af+/v7o3Lkzli9fjkWLFsHS0hJeXl7Yvn27qLWsX78e4eHhWLp0KTQ1NQEAffv2RVRUFJYvXy5qLX369MGECRMwb948ZGZmIjY2Fr169UJYWBhWrlwpai0AEB8fj2HDhqF169Zo0aJFsf/EFBsbiz59+sDMzEzltQBAREQExo8fD0NDQyQmJiI3NxcaGhqYNWsWdu3aJXo9165dg7OzM5KTkxEZGYkPHz4gISEBrq6uiIiIELWWjIwMuLq6onfv3pg6dSrS0tLg5+cHJycnUX4ROnHiBLy9veHt7Y3k5GQsXLhQ/ufC/2bMmIHPPvtM6bUUValSJeTk5Ih6z9Ko8rVP6UcYT5w4EXp6evD19UXbtm0RHh4OAwMDzJkzB8+ePcNPP/2kzNsrsLKyws6dO2FiYgJ3d3dUqVIFa9aswaNHj9C3b1/cuHFDtFqAglTar18/jBkzBitXrsT58+dx5MgRnDt3DosWLcLZs2dFq6VDhw7w9/dH9+7dFa4fP34cfn5+uHTpkmi12NnZYenSpWjXrh0sLCwQHh4OIyMjxMbGYurUqYiKihKtFqBgOmDu3LlITEzE27dvMW7cOEyYMAFaWlqi1gEUhJMaNWpg9OjR0NbWLvZxKysr0Wr55ptv0KxZMwwaNAhVq1ZVaS0A4OzsjO+++w69evVS+Lk5fPgwAgICcOrUKVHrGTRoEJydnTFixAiFerZv3459+/bhyJEjotUyY8YMZGZmYtmyZbCxsUF4eDiqV6+OGTNmQFNTExs3blTq/dPT07FixQoAwMGDB+Hg4FDsZ6ZatWro3bs3zMzMlFpLUYsXL8aBAwfQvXt3GBoayt+AC02aNEm0WgDVvvZpKO0r/3+xsbHYs2ePQuKrXLky3N3dRR9mFQQBlStXxvv37xEdHQ0fHx8ABam5WrVqotYCAElJSXBwcAAAnDlzBt9++y0AoFmzZkhPTxe1FkEQUL9+/WLXjY2N5dMYYklLS0O9evWKXa9Zs6ZK5vgSExPx8uVL6OjoIDc3F7///jvS09NhaGgoei0JCQk4fPgwGjduLPq9P/b8+XMEBgbC2NhY1aUAAB4/fow2bdoUu25mZobU1FTR67l//z5sbGyKXbezs8Pq1atFrSUyMhI//fQTatasKb+mq6sLb29vDBkyROn319XVxZIlSwAAhoaGGDNmjEpecz/2+++/w9TUFM+fP8fz588VPiaTyUSvR5WvfUoPA1WrVkVaWlqxF4zExMQSf7NRpvbt22PevHmoVq0aKlWqhB49eiA6OhqLFi2Cra2tqLUAQIMGDXD16lXo6+sjMTFRXsPhw4fRpEkTUWuZNGkSfHx84O/vjy+++AJAwRSPn58f3NzcRK2lffv22Lp1KxYuXCi/lpmZidWrV8Pa2lrUWkaNGoWbN29iwoQJ+O6775Ceno6FCxeiZ8+e+O677+Dh4SFqPS1atMDDhw/VIgz06tULR48eFf23p09p2rQpIiMjMWzYMIXrBw8eRNOmTUWvx9DQEHfu3IGRkZHC9fPnz6skSJYU6tPT06GhofS3AQWTJk1CZmYmbt68idzc3GJ9C+3atROtFjFHpstDla99Sv8pGDJkCObPnw8vLy8ABSEgJiYGa9aswcCBA5V9ewX+/v748ccfkZKSgvXr10NbWxu///47bGxsMHXqVFFrAYApU6bAy8sLeXl56NatG1q3bo1ly5YhNDQU69atU/r9TUxMFNKvIAhwcnKClpYWKlWqhLdv30Imk+GPP/7A2LFjlV5PIV9fX0yaNAmdOnXChw8f4O7ujpSUFDRo0EDpw5kfy8/Px8GDB/H5558DAPT19bF+/XpERERg8eLFooeB3r17Y+7cuejXrx8aN26MypUrK3y8T58+otUybtw4DBgwAAcOHIChoWGx36R27twpWi0A4O3tDTc3N1y5cgU5OTkIDAzE48eP8euvv4r+cwMA06ZNw6xZs3Dnzh3k5eXh0KFDePr0KY4ePSp674uTkxP8/PywcOFCyGQyZGVl4cqVK/Dx8YGjo6OotYSHh8PHxwfv3r0r9jGZTIa7d++KWs/du3fx4MED5OfnAyh4HczOzkZ8fLzovWQlvfYlJyfD0NBQ6T/DSu8ZAArS19atW/Hnn38CAOrUqQNXV1eMHTsWlSqpdnVjeno6dHR0VDIkVHj/1NRUecNVQkICatasCT09PaXf++rVq+X+e4s9/wsA0dHRSEhIQG5uLoyNjdG5c2eV/7wUlZmZKfroVmkjWDKZDGfOnBGtlkGDBuH169fo0aNHiT0DqhgxePHiBXbt2oWHDx8iLy8PxsbGGDZsGBo0aCB6LUDBCqHg4GCFelxdXWFubi5qHdnZ2Vi9ejVCQkKQk5MDmUyGzz77DAMGDMCsWbNK/P4pS7du3WBvb48pU6aI/u/nY+vWrcO6deugp6eHtLQ06Ovr4+XLl8jLy8PXX3+NgIAAldSlitc+UcIAUDBElZeXh7y8PLx580Yl/zhTU1OxdOlSjB8/Hp9//jnGjh2LuLg41K9fHxs2bICJiYnoNT18+BD16tVDjRo1EBkZibNnz6Jly5aij5qoo5cvX5a4nEbsn53w8HBs374dSUlJOHjwIHbu3Im6deti/PjxotahbszNzXHgwAH5tBKpv/fv3+PJkyfIy8uDkZERqlevjvT0dOjq6opWQ5s2bXDkyBE0bNhQtHt+SpcuXTBp0iQMHjwYtra22LFjB2rVqgVPT0+0aNEC06dPF72mkJAQ1KpVC05OTgAADw8PdO7cGUOHDlXqfZU+TfD06VNMmzYN1tbWmDFjBgDA3t4ejRo1wo8//ggDAwNllyDn6+uLrKws1K5dGwcOHMD9+/cRGhqK8PBwLFq0CCEhIaLVAgC7d+/GwoULsW3bNmhra2PixIlo3749Tp06hZSUFKVPXdjZ2WHfvn3Q0dGBra1tqaMEYv7GeeLECfj4+OD169cK1wVBEH0YcdeuXdiwYQPc3Nzk3dCtWrWCv78/srOzVfLb7/PnzxESEiL/bfPzzz/HwIEDRe8zsbS0xMOHD9UmDDx8+BCrV69GQkJCiSFSzJ9hoOD7FBQU9Ml6xJxGadGiBaKioqCrq4tmzZrJrycnJ8PJyUnUlVTdu3dHREQExowZI9o9P+Wvv/5Cly5dABQ8Rzdu3ICzszM8PT0xZcoU0cPAmjVrsH//foWeAWtra2zYsAHp6elKnZZUehjw9fWVd48WOnbsGHx8fLBgwQJR5/KuXLmCAwcOoH79+jh9+jTs7Oxgbm4OXV1deQoTU1BQEJYtWwYrKyssWrQILVq0QFBQEK5duwZPT0+lh4FJkyahevXqAIDJkyfLr2dkZEBTU1MlS+cAYMmSJXB0dMSIESNEHb4syU8//YTFixejW7duWLVqFYCCefvatWtj/vz5ooeB2NhYfPfdd2jevDnatGmDvLw8XLt2DT///DOCg4NhaWkpWi2dO3fG7NmzERERASMjo2JrxMV+bn744QdUrVoVI0eOVPnPDQB4enrixYsXsLe3V0k9hw4dwoEDBwAUBGkPD49iPSbPnz9H3bp1Ra1LX18fa9aswfHjx0vseylcdSBWLU+ePEGDBg3wxRdfID4+Hs7OztDW1hZ9RRcA7N+/H//5z3/Qtm1b+bWRI0eiefPmmDFjxr87DMTFxSEsLAx16tSRX9PR0YGnpyf69++v7NsrqFKlCj58+ICMjAxcvXpV/uL+9OlT1KpVS9RagIJpi8IX73PnzmHw4MEAAAMDA7x9+1bp9y+6tLNnz57YvHkzQkND8fLlS8hkMhgYGMDV1RWjRo1Sei1FZWVlYeTIkWqxZC0lJaXE33yNjIxK3EVN2ZYuXYoRI0bghx9+ULi+cuVKrFixAqGhoaLVcu7cObRo0QKpqanFlu6pogfn0aNH2L9/v9qMVPz2228IDQ1VyfQjAHz99dd4+vQpACAmJgZt2rSRh/9C1apVw9dffy1qXRkZGSr55askAwcOxPfffw9/f3/06NEDrq6uqFevHi5fvqyS79u7d+9K7KPQ0dFR+q69Sg8DOjo6iI+PR6NGjRSuJyQkiN480qNHD0ybNg1Vq1ZFrVq10K1bNxw7dgz+/v4q2Vr2888/x+HDh6Grq4uUlBT06NEDOTk5CA4OFv0HcfHixbh06RKmT5+Oli1bIj8/H7dv30ZAQADS0tLw/fffi1bLsGHDsG3bNsydO7fYJiBiMzc3x6FDhxRGTgRBQHBwsKiboxR68OBBiTsfDhgwQPRlUuq2LKtwN091CQPm5uZISkpSWRioXr26fHTG0NAQPXv2VPm/J0Dc3/zL4ubmBgMDA2hpacHMzAze3t4IDQ1F7dq14e/vL3o9Xbp0gZ+fH5YtWybvjUpNTcWyZcvQuXNnpd5b6Q2E27Ztw4YNG+Dq6gpTU1MABR2227dvx5gxY0RtwsrNzcXPP/+M5ORkDB48GE2bNsWhQ4eQmZmJ4cOHi/7bTHR0NKZNm4aMjAwMGzYM8+fPx8KFCxEREYHAwEC0atVKtFosLS2xadMmheEpAIiKisL333+Pq1evilbL3bt3MWrUKLx//x56enrFvi9izv3ev38f48ePR506dXDv3j106NABiYmJeP/+PYKCgkTfdtfR0RFubm5wdnZWuB4WFoaAgADR58XVaVlWSkoK+vbtiy+//LLEpY5ivwk9ffoUQ4cORadOnUqsR+xpFHX6XsXFxWHHjh14/PgxAgMDcfjwYXlgkbL09HS4u7vj1q1b8tHqjIwMtG/fHitWrFDqKjOljwyMHj0aWlpa2LNnD4KCgqChoYHGjRvD29sbvXv3VvbtFWhoaMDV1VXhWuG67JycnGJzV8rWoUMHREdH482bN/JvvLu7O7y9vUWvRVtbu8TNR2rUqCH6piQzZsxAs2bN4OTkpPK53y+//BLHjx9HeHg4Hj16hLdv38LCwgL29vYKjVhiGTduHHx8fJCQkCAfmbh16xZ++uknUUdvgLKXZYlt3rx5qFSpUokBUhXWrFmDv/76CwkJCcX2/xe7PnX6XkVERMDb2xuDBg3C+fPnFc6QKPzFSEwfrxb66aefoKenp5LVQrq6uggNDcW9e/fw6NEjaGhooEmTJuJsmiVIyIsXL4TFixcLrq6ugouLi+Di4iKMGDFCGDx4sNC2bVuV1JSWlibExsYKMTExQkxMjHD16lUhMjJS2LRpk9LvnZycLP8vKChIsLe3Fy5cuCCkp6cLGRkZwrVr14RevXoJv/zyi9JrKcrc3FxISkoS9Z6fEhsbK3Tu3FmIjo4WUlNThU6dOglt27YVTE1NhWPHjqmkpv379wt9+/YVzMzMhHbt2gmDBg1SSS2dO3cWQkNDBUEQhO7duwtJSUlCRkaGMGbMGGHFihWi12NmZib89ttvot/3U8zNzYWrV6+qugxBENTre9WrVy8hPDxcEARBaNOmjfzfenh4uNCjRw9RawkJCRE6deok/PTTT4KZmZmQlJQkHDp0SLCyshLWrl0rai1FPX/+XEhJSVF4jU5OTlbqPZX+K58gCDhz5gwePHiAvLw8+fXC4amgoCBllyA3e/ZsJCUlwd7eHsHBwRg9ejSSkpJw6tQpzJo1S7Q6Cu3ZswcLFy5Ebm4uZDKZfFtOmUwGMzMzpSfTossJC+89fvz4YtcWLFggyv7lhbp3747Lly/LGypVyd/fH46OjjA3N8fWrVtRpUoVnD17FkePHkVAQID8bAkx9evXD/369RP9vh9Tt2VZzZo1K7YcVZUaNGigshU5H1On75U6nSGhbquFLl26hPnz5+PZs2cK1wURllUrPQwsWrQI+/btQ8uWLXH79m1YWFggKSkJL1++VPomCh+7du0agoODYWFhgaioKHTr1g2WlpbYvHkzLl68iJEjR4paT2BgINzc3DB+/HjY2tpi7969ePv2Lby8vEQZuhN7frm8DA0N4efnh0OHDpW4ZE3Mud8HDx5g7dq10NLSwtmzZ2Fvbw9NTU1YWVnB19dXlBrWrVuHsWPHQktLq8xtqsV88VK3ZVlDhw6Fl5cX+vXrh4YNGxab3hJzq2agYLvxWbNmwdXVtcR6xNyDX52+V+p0hoS6rRZatGgRzMzMsHHjRtEb7JUeBo4dO4aVK1fC3t4e3377LXx9fWFsbIxZs2aJfo60IAjQ19cHUPADGR8fD0tLSzg4OGDr1q2i1gIUrPHt06cPNDU1YWpqips3b8LBwQGzZ8/GnDlzMG7cOKXeXxWHpZRHWlqa2jQS6enp4Y8//kBWVhbi4+PlI0iXL18u8ZRHZbh69SpGjhwJLS2tUhs5xZ6HVrdlWevXr4eGhgbCw8OLfUwmk4keBqZNmwagoJehpHrE3DxLnb5X6nSGhLqtFvrzzz8RFBRU7HArMSg9DGRmZsq74r/88kvcvn0bzZo1w4QJE0Q9/AYAWrZsibCwMEycOFG+I5eLi4t8La7YdHV1kZ6ejoYNG+Lzzz/H3bt34eDgAH19fZUcuaou1GnpkaurKzw8PFCpUiW0bt0aVlZWCAwMxLp160Srs+gSvmXLlsHAwKDYPuV5eXm4d++eKPUUUrdlWWfPnhX9nqUR+/tRGnX6XrVt2xbHjx/Hrl27AACvXr1CmzZtsHz5ctG3Gp87dy7Gjx+P8+fPIzs7GwsWLMCjR4/w/v17bNmyRdRagILnJi4uTiVhQOlLCx0cHPDDDz+gR48eWLt2LV6+fIkFCxbg/v37GDx4sKjbYMbFxcHNzQ0eHh7o3bs3evXqBR0dHaSkpMDZ2Rk+Pj6i1QIUvOldvHgRfn5+eP/+Pby8vDBv3jycO3cOd+/eRVhYmKj1qAt16jMBCpZkJScno3PnzqhatSpu3ryJqlWrquS336Lbyhb1+PFjODs749atW6LXpErXrl2DhYUFNDQ0cO3atU8+TiaTFVs2qwwpKSmoX78+ZDIZUlJSSn2sqg5PUrXDhw+jR48eatNP8eHDB4SHhyMhIUF+mJSzs3OxDZrEEBgYiE2bNsHGxqbE3RmVOQ2o9DCwd+9e+Pv7w8/PD82bN0e/fv0wYMAA3LhxA7q6uqK/sGdmZsrXr6empuL06dOoXbs2HBwcRD8RLycnB5s2bUKLFi1gZ2eHNWvWYPfu3fK0/tVXX4laj7pYuHBhqX0m8+fPV3WJotq7dy8CAwMBFOwlX79+/WI/q69fv4aRkZF8+1mxqHpZlomJCaKiolCnTp1Sw5lYw/If11O0MbiwDjGawYCC4fjyEnM0zsbGBhkZGejatSucnJxgY2ODKlWqiHb/ogICAtCzZ0+12ajKxcXlkx+TyWRKPc9ClFMLr127hmrVqsHU1BSRkZHYu3cvateujcmTJ4u+Lzapv/bt22PhwoXyPpO1a9fK+0y0tLSwaNEiVZcoqpycHBw9ehT5+fmYPXs2Zs+ejRo1asg/LpPJoKWlhfbt24u6rfbHhzgdOXIE169fh7+/P1xcXFRyiJOqFQ1rH+8t8DFl9+wUDQPv3r3DiRMn0Lp1a7Ru3RqVK1dGfHw8rl+/jj59+sDPz0+ptXzsxo0biIiIQEREBP766y/Y2trC0dERXbp0EXWPFTc3N0RFRcHY2BhOTk5wdHRUi9MUVUG0I4xVpTCdl4cYvzmU1Q1elBRfTIGCUwEjIiLQoEEDTJkyBTY2Nujfvz8ePHiAsWPH4uLFi6ouUWViYmLw1Vdfib4RVEkcHBwwc+ZMdOvWDRYWFggPD4eRkREuXLiA+fPn48KFC6LWY2dnh/3796N27doK11NTU9GnTx9ER0eLWs/IkSOxbt061KxZU+F6eno6xo0bJ+oozrRp09C0adNirylBQUGIjo5WSQN1od9++w0nT55ESEgINDQ0RN3tFCgYLT516hROnDghb6js2bOnvH9LbKraKVIpryguLi7lfgNW9jGeYh4TWh7l/UFXhx3UVMXIyAjx8fFo0KABmjVrhtu3b6N///4QBEHph3Wou3bt2qlNP4U6LMs6ceKEPHQkJydj4cKFxYack5OTiy1PVZaLFy/i9u3bAApGRAMDA1GtWjWFxzx+/LjMUYN/2vnz5+WrG4qys7PD2rVrRa2lUFZWFs6fP4+IiAhcunQJ+vr6cHR0FL0ObW1t9O3bF3379sWbN2+wdetWrFmzBsuXL4elpSUGDx4s2sFKqtwpUilhwNrautg1QRDw6tUryGSyYsldmaysrBT+fOHCBVSqVEm+AYefnx+6dOmCrl27ilJPSYe7fPjwQf4ClpKSItnGokJjxozB9OnT5Rv+9OvXDxoaGrh+/bpk+ygKqdO+HaUty2rdurUoNVhZWSmMQJQ00NmsWTPRNtUxNjZGUFAQBEGAIAi4fv26wrC3TCZDtWrVRB+WNzY2xv79+xVOuxQEASEhIWjevLmotRw8eBARERGIiopC3bp14ejoiJ9//lllBzoBBdMWJ06cQEREBDIyMmBvbw9HR0e8ePECq1evxsWLF7F8+XKl17F7924sWLAAgwcPhq2tLXbs2IFatWrB09Oz2GF//zil7m8oCEJubq6wevVqoUOHDkLz5s2F5s2bC127dhVlu92P7dy5U7CwsBAOHDggv7Z06VLBwsJC2L17t+j1PH36VOjfv7+wfPly+bX27dsLgwYNEv7880/R61EnMTEx8q1lIyMjhcmTJwvz588XXrx4oeLKVMva2lo4efKkIAiC8M033wj3798XcnJyhB9++EGYO3euqLXcv39fsLGxEfr16ye0bNlSGDt2rGBnZyd07NhRiI+PF7UWQRCEtWvXCm/fvi3zcYcPHy7X4/5Xs2bNEt68eVPm42JjY4UPHz4otZZr164JlpaWgr29vTB58mRh8uTJgq2trUq+V126dBH8/f2FW7duCa9evRJyc3OF/Px8UWsotHjxYsHGxkZo1aqV4O7uLhw9elR4//69wmOOHDkitGnTRpR6TE1N5dsOu7u7C2FhYYIgCMKdO3eE7t27K/XeSu8Z8Pf3R0REBKZMmYJWrVohPz8fd+7cQUBAAAYPHizqvLitrS3mzZuH7t27K1w/c+YMlixZgtOnT4tWCwCMHTsW2tramD9/PurUqQOgYNtQHx8fZGdnyzvIpeb169cIDg7GnTt3kJubK/8tC1B+R626U6d+Cm9vb8yZMwcnTpzAw4cP5cuybGxssHTpUgQEBIhWy9/x1VdfISwsTCVruUsiVj3p6ek4fvw4Hj58CKBgxKRnz57FehqULT8/H4GBgdixYwfevHmDkydP4scff0S1atVEP7Z8zJgx6NmzJ+zt7RWacotKSkpCcnIyOnTooPR67Ozs4O/vD2tra6xevRrZ2dmYNWsWHj16hD59+uDmzZtKu7fSu5AOHjyI9evXKwzXm5iYwNDQENOnTxc1DPz1118lDrUYGxvj5cuXotVR6Pr16wgLC5MHAQDQ0dGBp6cn+vfvL3o96sLLywt37txBr169RN+SU92pup/ixo0bePz4MQDg0KFDMDU1hba2tsJQc2hoKC5duqT0Wv5bSv79528Tqx5dXV0MHz681MeIEUw2btyII0eOYOnSpfD09AQA9O3bF/Pnz8fy5csxd+5cpd37Y8HBwWU+plGjRujTp48ogU2VO0UqPQxoaWmVuFSkZs2aojfJWVpaYu3atViyZIl8w4sPHz4gMDAQFhYWotYCFLzxx8fHFwsoCQkJkn4TvHz5Mn7++WeVbAeq7lTdT6GlpYW1a9fKR2uCgoIU9jwonBMX+5Ai+meIEUwOHDiApUuXol27dvL3gE6dOmHZsmWYOnWqqGGgvMQKbKXtFKnsvSCUHga8vLwwe/ZseHl5yXcKu3fvHvz8/DBq1CiFXbqU3Tg3f/58jBkzBp07d0aTJk0AFAwB6enpYcOGDUq9d0lcXFwwb948PHz4EKampgAKtjDdvn07xowZI3o96kJfX1/0DaD+LQYOHIgmTZqgevXq+OKLL7B+/Xrs2bMHZmZmCo18ymJiYiI/4MrFxQXr1q0TdW8D+vdLS0tDvXr1il2vWbMmsrKyVFCR+jh06BAcHR3lUyUDBw7EwIEDkZWVhX379sHY2Fhp91Z6z0DRoY2Pj8YtvCaItCMXULAEKzIyEo8ePYKGhgaaNGmCzp07Kyw9+vPPP1GvXj1R3pBCQ0OxZ88eJCYmQkNDA40bN4aLiwt69+6t9Hurq1OnTmHTpk2YMmVKiVtySnm1Bfsp/ndF90RQB+pUjxi1uLm5oV69eli4cKH8fjo6OvLRJHXslVLm85Keno73798DKOgZ2LdvH3R0dBQec+/ePUybNk2+bFUZlD4yoG7H5GpqasLOzq7Uxzg6OorWYDRkyBAMGTKk1Mf4+vpiypQpxfajr6gKf8MdP368wlSSmKFRXbGfgv7tfH19MWnSJHTq1AkfPnyAu7u7fEm12KcWqoOYmBhMmzZN/lo3YMAAhY8Xhn1nZ2el1qH0MKCux+SWRt0ajMLDwzF27FjJhAF1C5DqhP0U9G9nYGCAffv2ITo6GgkJCcjNzYWxsTE6d+4syenBb7/9FmfPnkV+fj569OiBvXv3KrzWF243/vFowT9N9XuaUpnULZwo278xQIqF/RT/u06dOolyYl7REwyLKjxuurBPyNjYWNT9+EsjZlN3hw4dRFmu909Q9vNSOPX58bHXHz58wO+//67UXoFCDANE/yJeXl7yaSP2U/x3Z338nc/5X9jZ2ZV43PTTp08xbNgw+XHTYp80WRqp/eJRXmI9Lw8fPoS3tzdmzZqFpk2bYvDgwUhMTISWlhY2btyI9u3bK+3eDANE/yLsp1Ckbmd9FD1uWhAE9O/fv8TjplV1ZG56ejo+fPhQ7M2tMESeOXNG1O3iVa28h1uJ9bz4+vrCyMgITZo0wb59+/DmzRtcunQJ+/fvx7Jly3Dw4EGl3ZthgOhfhP0Uiko660OV+vTpg8qVK8uPmx49evQnj5sWU3R0NLy8vIptrvZxiJRCX9J/c7iVWM/L7du3ceTIEejq6uL06dP4+uuvoaenBycnJ6Uvf2cYKIGUTwwk9cZ+itKp6vjXQpUrV0afPn0AAA0bNlSb46YXLFgAa2trjBs37pPb7kqFuh1uVVSNGjXw8uVLaGho4ObNm5gwYQKAgp/rojvVKoPqf0rVkKamJgMB0b+MKo9/LYmVlRXi4uKwY8cOPH78GIGBgTh8+DAMDQ3Rs2dPUWtJSUnBli1b1GIvA1XT1dWV7+ZnaGiIMWPGFDtmWlX69euHiRMnQlNTEw0bNkTnzp3xyy+/YPny5Zg6dapS7y25MPDmzRuEh4cjMTER7u7uuHXrFr744guFLYGvXLmiwgqLmzp1qtKXlRD926n0+NcSREREwNvbG4MGDcL58+eRm5sLDQ0NzJo1CxkZGRg2bJhotVhbWyMuLo5h4COTJk1CZmYmbt68Kd/Eq6h27dqJWs/333+P1q1bIzk5GU5OTvjss8/QoEEDrF69utgBe/80pe9AqE7u37+PUaNGoX79+rh//z6OHz+ODRs24MSJE9i0aZPCYUpiKGk3uaK4mxxR+RU90dHDwwPffPMNnJ2d8euvv2LKlCk4e/asqPU4Ozvju+++Q69evRR2sDt8+DACAgJw6tQppd6/6KqJ1NRUhIWFwd7eHo0aNSrW1CjmgXHqJDw8HD4+Pnj37l2xj0mtIVdSIwOLFy/G0KFDMWXKFPnBREuWLIGuri6WL1+Offv2iVoPd5Mj+ufo6+vjyZMnaNCgAb744gvEx8fD2dkZ2traSE9PF72ex48fo02bNsWum5mZITU1Ven3/3ilhbm5OVJTU4vdW8pToqtXr8bAgQMxZcoUlb0GF92C2NbWttTvhzIbiCUVBu7cuYPFixcXuz5kyBCEhISIXg93kyP656jy+NeSNG3aFJGRkcWmAw4ePIimTZsq/f5FV1qkpKTAwMCg2IhA4QZIUvXq1SuMHDlSpb+MTZo0CdWrVweAUg8bU3Zok1QY0NXVRWJiYrH5w+vXryu9U7Mk3E2O6J9T2vGv/v7+otfj7e0NNzc3XLlyBTk5OQgMDMSjR4/w66+/in4YT3k3QJKa7t27IyIiQqWnxB44cKDc+wcUrlRRBkn1DISGhmL9+vVwc3PDihUrMGfOHDx79gw7duyAp6cnRowYIWo9PJ2PqGJ7+fIlQkJC8PDhQ+Tn58PY2BjDhg1D/fr1lX7vohsgJScno379+iVugGRkZKRWuyCKaenSpQgJCYGJiUmJr8GFqw6UqWhvx19//YXdu3ejR48eaN26NSpXroy7d+/i2LFjGD58OLy8vJRWh6TCAACcPXsWW7duxcOHD5GXlwdjY2O4urrC0dFR9FpKOt4ZkO5uckR/l7e3N+bMmQNtbW14e3uX+lgxXtiL+rhBOD8/X+HfubIbhHNycnD06FH5BkizZ8/+5AZItWrVUmot6krdfmZGjRqFb775ptjU0oEDB7B7927s3r1bafeW1DQBANja2sLW1lbVZQDgbnJEFZmqG4SLboCUlpYGe3t7GBgYiF6HOhP7zb4st27dgq+vb7Hr5ubmWLhwoVLvLamRgU+lQJlMhsqVK6Nu3bqwt7fHl19+KXJlRPRPyM3NRUZGhrwH6MaNGzA1NYWmpqbotZiZmalNg3C7du1w4MAB7jNQAnXZGAoAhg0bhsaNG8PX11e+RXJmZibmzJmDjIwMbN++XWn3llT3WvXq1XHo0CEkJiaiVq1aqFmzJp48eYIDBw4gLS0Nd+7cwcCBA3Hu3Dml1dCiRQukpaUBKJgmaNGixSf/I6Lyu3v3Luzs7LB161b5tenTp8PBwQF//PGH6PWoU4Nwz549sXHjRjx69AjZ2dmqLkdtREREYPz48TA0NERiYqLCxlC7du0SvZ5FixYhJiYGnTp1Qv/+/dGvXz907doVDx8+hJ+fn1LvLamRge+++w6tW7fGlClTFK4HBgbi5s2bCAwMxN69exESEoJDhw4ppYaYmBj5fuUxMTGlPlbsTZCI/s2GDh0KU1NTzJw5U94Ilp+fD39/f/z++++iH2qkTg3Ctra2SElJ+eTyNKn2J6l6Y6iSZGdn4/Lly3j48CGAgnMSOnbsqPQzLiQVBtq0aYNDhw6hSZMmCtcfPXoEZ2dn3L59GykpKXBwcFCrpTZfffUVwsLCOMRHVIo2bdrg8OHDxf6dJCUloXfv3rhx44ao9ahTgzB/8SiZubk5jhw5AiMjI4Uw8PjxY/Tq1Qu3b99WdYmikVQDoZGREU6ePCk/CarQqVOn5Et9Hj16pHbHeEoorxH91+rXr4/o6OhiYeD69evQ09MTvR51ahCW6pt9WVS9MZQ6kVQYmDlzJtzd3XHp0iW0atUKAPDrr7/i5s2bWLt2Le7evQtPT0+VbkBBRP8dNzc3zJkzBzdu3JD/+7537558/3mxqfq4aXXZ5ladlbQx1OPHj/Hrr79i48aNqi5PVJKaJgCAJ0+eYN++ffj999+hoaGBpk2bYvDgwdDT08OjR4+QlJQEOzs7VZepoOjwFRF9WmRkJPbs2YPExERoaGigcePGcHFxQdu2bVVdmugOHjyInj17QlNTU2GHu4yMDGhqakJLS0t+rW/fvqooUS28ePECu3btUth7ZtiwYZLb9E1SYeDly5fYtGkT/vjjD+Tl5cmH33NycvDw4UNcu3ZNxRWWjGGAiP4X2dnZ2Lx5M0JDQ/Hy5UvIZDIYGBjA1dUVo0aNUnV5KnP48GH06NFDIRhJlaSmCWbPno2kpCTY29sjODgYo0ePxpMnTxAREYFZs2apujwi+pvUeQdCdbJ48WJcunQJ06dPR8uWLZGfn4/bt28jICAAaWlp+P7771VdokqsXLkS8+bNQ9euXeHk5AQbGxv5+n6pkVQYuHbtGoKDg2FhYYGoqCh069YNlpaW2Lx5My5evIiRI0equsQSSfmIUSL63x09ehSbNm1SmC4xMTGBoaEhvv/+e8mGgQsXLuDGjRuIiIjAsmXLMGvWLNja2sLR0RFdunQpthy0IpNUGBAEAfr6+gAKukjj4+NhaWkJBwcHhY1K1I2EZnKI/pbk5GS8f/8e2trasLa2hoODg2R/syuNtrZ2ievUa9SoofT16+rOwsICFhYWmDlzJn777TecPHkSM2bMgIaGBq5evarq8kSjHttjiaRly5YICwsDULATYFRUFICCYzxVJS8vD+fPn8f27dvx+vVr3Lp1C2/evFF4zJkzZ1TemUykjm7duoUXL14AKJgyePv2rYorUh8pKSny/0aOHImZM2fi4sWL+Ouvv/D69WvExsZi7ty5mDx5sqpLVbmsrCwcO3YMW7Zswa5du6Cvrw8XFxdVlyUqSTUQxsXFwc3NDR4eHujduzd69eoFHR0dpKSkwNnZWfTlR8+ePcPYsWPx6tUrZGRk4MSJE1i+fDlu3LiBrVu3onnz5qLWQ/Rv4+7ujqioKNSpUwcpKSklHtNbSGrL50xMTORTjEVf5j++JuUTUg8ePIiIiAhERUWhbt26cHR0RM+ePRU2jJIKSYUBoODQh/fv30NPTw+pqak4ffo0ateuDQcHB9H3EZ84cSL09PTg6+uLtm3bIjw8HAYGBpgzZw6ePXsm+vapRP82mZmZuHLlCt68eQNvb+9ix/QWJbXlc8nJyeV+rFRHHrt27QoHBwf07NkTjRs3hra2NipVqiTJPi3JhQF10q5dO+zZswfGxsYKywcfPXqEvn37ir59KtG/jZWVFcLCwlC/fn3Y2toiPDxcJccF079Tfn4+AgMDsWPHDrx58wYnT57Ejz/+iGrVqmHu3LkqOe1SVSTVM6BuqlatKj/BsKjExES+oBGVQ35+PqKiopCcnIxnz57h8ePHCnPlRf8j+tjGjRtx+PBhLF26VP7G37dvX0RFRWH58uUqrk5c0m4jVbEhQ4Zg/vz58PLyAlAQAmJiYrBmzRoMHDhQxdURqb9Ro0Zh7ty58mHd/v37l/g4Kc+L06cdOHAAS5cuRbt27eQ/Q506dcKyZcswdepUzJ07V8UViodhQIU8PDxQs2ZN+Pr64t27dxg/fjzq1KkDV1dXjB07VtXlEam9yZMnY9SoUXjz5o18L/4qVaogLy8PeXl5+Oyzzz7ZQ0CUlpaGevXqFbtes2ZNZGVlqaAi1WHPgBr48OGD/MXrzZs3ktsTm+ifkJiYiJCQEISGhiIvLw8A8Nlnn6FXr15YsGCBpOZ/qXzc3NxQr149LFy4UN63paOjg+nTpwMAAgMDVVyheNgzoEJPnz7FgAEDEBAQgGrVqqFGjRro378/Bg8ejD///FPV5RH9q4SEhODChQvYuHEjrl27hqtXr2L9+vWIjY3FmjVrVF0eqSFfX1/Ex8ejU6dO+PDhA9zd3WFjY4Pk5GRJTREAHBlQqXHjxqF69eqYP38+6tSpAwD466+/4OPjg5ycHMkdoUn0v2jfvj1+/PFHWFtbK1y/cuUKpk+fjkuXLqmoMlJ30dHRSEhIQG5uLoyNjdG5c2fRl5qrGnsGVCguLg5hYWHyIAAAOjo68PT0/GQjFBGVTBAEhX9LhXR1dbkzIZWqQ4cO6NChg6rLUClpRR81o6Ojg/j4+GLXExISuLSQ6G9q3749Vq5ciczMTPm1169fY/Xq1cVGC4hIEUcGVMjFxQXz5s3Dw4cPYWpqCgC4d+8etm/fjjFjxqi4OqJ/l9mzZ2PkyJHo0qULjI2NARQ0FRoZGXHKjagM7BlQsdDQUOzZsweJiYnQ0NBA48aN4eLigt69e6u6NKJ/nZycHFy8eBEJCQmoUqUKjI2N0alTJ8nN/xL9XQwDREREEsdpAhUSBAFnzpzBgwcP5OuiASA7Oxvx8fEICgpSYXVERCQVDAMqtGjRIuzbtw8tW7bE7du3YWFhgaSkJLx8+RJDhw5VdXlERCQRnEhToWPHjmHlypUIDQ1Fo0aN4Ovri3PnzqFnz57IyclRdXlERCQRDAMqlJmZiVatWgEAvvzyS9y+fRsaGhqYMGECLly4oOLqiIhIKhgGVMjIyEi+z0CzZs1w+/ZtAAW9BG/evFFlaUREJCHsGVChMWPGYMaMGfDz84OjoyP69esHDQ0N3LhxA5aWlqouj4iIJIJLC1Xs2rVrqFatGkxNTREZGYm9e/eidu3amDx5MurWravq8oiISAIYBoiIiCSO0wQic3FxgUwmK9djd+7cqeRqiIiIGAZEV9KBKYIg4NWrV5DJZKhdu7b4RRERkaRxmkCF8vLyEBAQgL179yI9PR0AoK+vj+HDh2P8+PEqro6IiKSCIwMqtGzZMkRERGD69Olo1aoV8vPzcefOHQQEBCA7OxuTJk1SdYlERCQBHBlQoXbt2mH9+vWwsrJSuH758mVMnz4dly9fVlFlREQkJdx0SIW0tLRQuXLlYtdr1qxZ7iZDIiKi/xXDgAp5eXlh9uzZOHfuHF69eoXMzEzExsZi3rx5GDVqFFJSUuT/ERERKQunCVTIxMRE/v+FIwFFvx0ymQyCIEAmk+Hu3bui10dERNLAMKBCycnJ5X6soaGhEishIiIpYxggIiKSOPYMEBERSRzDABERkcQxDBAREUkcwwAREZHEMQwQERFJHMMAERGRxDEMEBERSdz/A9QOt+OO7B9WAAAAAElFTkSuQmCC\n"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#checking the nulls in the df\n",
    "sns.heatmap(df.isnull(),cbar=False,cmap='rocket',yticklabels=False)\n",
    "plt.title('Missing values on the split dataset');"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "outputs": [],
   "source": [
    "#treating the nulls in the net time. When net time is null, net_time = official_time\n",
    "df.loc[df['net_time'].isnull(), 'net_time'] = df[df['net_time'].isnull()]['official_time']"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "outputs": [],
   "source": [
    "#treating the nulls in the team. When net team is null, team= Individual\n",
    "df.loc[df['team'].isnull(), 'team'] = 'Individual'"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/zk/75k1z4rs6_g2dwpqhz8rs1500000gn/T/ipykernel_11462/806395404.py:2: UserWarning: Parsing dates in DD/MM/YYYY format when dayfirst=False (the default) was specified. This may lead to inconsistently parsed dates! Specify a format to ensure consistent parsing.\n",
      "  df['birth_date'] = pd.to_datetime(df['birth_date'])\n"
     ]
    }
   ],
   "source": [
    "#Converting columns type\n",
    "df['birth_date'] = pd.to_datetime(df['birth_date'])\n",
    "df['net_time'] = pd.to_timedelta(df['net_time'])\n",
    "df['official_time'] = pd.to_timedelta(df['official_time'])\n",
    "df['event_year'] = pd.to_numeric(df['event_year'])"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "## Searching for irregularities"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "In this section we will search for irregularities in the dataset such as:\n",
    "- Men that runned in a female run;\n",
    "- Women that runned in a masculine run;\n",
    "- People that were in an age class that was not in the correct age\n",
    "- Names that are not registered corrected.\n",
    "\n",
    "To perform that we searched that for instance, if a age class is M50, that means tha are running only men in the 50ths."
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "outputs": [],
   "source": [
    "#creating new columns to perform the check\n",
    "df['class_gender']=df['age_class'].astype(str).str[0]\n",
    "df['class_age']=df['age_class'].str[-2:]\n",
    "df['age']= df['event_year'] - pd.DatetimeIndex(df['birth_date']).year"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/zk/75k1z4rs6_g2dwpqhz8rs1500000gn/T/ipykernel_11462/3250346233.py:1: PerformanceWarning: Adding/subtracting object-dtype array to TimedeltaArray not vectorized.\n",
      "  df.loc[df['age_class'].isnull(), 'age_class'] = df['sex']+df[df['net_time'].isnull()]['official_time']\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for +: 'NaTType' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001B[0;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[0;31mTypeError\u001B[0m                                 Traceback (most recent call last)",
      "Cell \u001B[0;32mIn [11], line 1\u001B[0m\n\u001B[0;32m----> 1\u001B[0m df\u001B[38;5;241m.\u001B[39mloc[df[\u001B[38;5;124m'\u001B[39m\u001B[38;5;124mage_class\u001B[39m\u001B[38;5;124m'\u001B[39m]\u001B[38;5;241m.\u001B[39misnull(), \u001B[38;5;124m'\u001B[39m\u001B[38;5;124mage_class\u001B[39m\u001B[38;5;124m'\u001B[39m] \u001B[38;5;241m=\u001B[39m \u001B[43mdf\u001B[49m\u001B[43m[\u001B[49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[38;5;124;43msex\u001B[39;49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[43m]\u001B[49m\u001B[38;5;241;43m+\u001B[39;49m\u001B[43mdf\u001B[49m\u001B[43m[\u001B[49m\u001B[43mdf\u001B[49m\u001B[43m[\u001B[49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[38;5;124;43mnet_time\u001B[39;49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[43m]\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43misnull\u001B[49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\u001B[43m]\u001B[49m\u001B[43m[\u001B[49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[38;5;124;43mofficial_time\u001B[39;49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[43m]\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/ops/common.py:72\u001B[0m, in \u001B[0;36m_unpack_zerodim_and_defer.<locals>.new_method\u001B[0;34m(self, other)\u001B[0m\n\u001B[1;32m     68\u001B[0m             \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mNotImplemented\u001B[39m\n\u001B[1;32m     70\u001B[0m other \u001B[38;5;241m=\u001B[39m item_from_zerodim(other)\n\u001B[0;32m---> 72\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[43mmethod\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mother\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/arraylike.py:103\u001B[0m, in \u001B[0;36mOpsMixin.__add__\u001B[0;34m(self, other)\u001B[0m\n\u001B[1;32m    101\u001B[0m \u001B[38;5;129m@unpack_zerodim_and_defer\u001B[39m(\u001B[38;5;124m\"\u001B[39m\u001B[38;5;124m__add__\u001B[39m\u001B[38;5;124m\"\u001B[39m)\n\u001B[1;32m    102\u001B[0m \u001B[38;5;28;01mdef\u001B[39;00m \u001B[38;5;21m__add__\u001B[39m(\u001B[38;5;28mself\u001B[39m, other):\n\u001B[0;32m--> 103\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m_arith_method\u001B[49m\u001B[43m(\u001B[49m\u001B[43mother\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43moperator\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43madd\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/series.py:6262\u001B[0m, in \u001B[0;36mSeries._arith_method\u001B[0;34m(self, other, op)\u001B[0m\n\u001B[1;32m   6260\u001B[0m \u001B[38;5;28;01mdef\u001B[39;00m \u001B[38;5;21m_arith_method\u001B[39m(\u001B[38;5;28mself\u001B[39m, other, op):\n\u001B[1;32m   6261\u001B[0m     \u001B[38;5;28mself\u001B[39m, other \u001B[38;5;241m=\u001B[39m ops\u001B[38;5;241m.\u001B[39malign_method_SERIES(\u001B[38;5;28mself\u001B[39m, other)\n\u001B[0;32m-> 6262\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[43mbase\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mIndexOpsMixin\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m_arith_method\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mother\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mop\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/base.py:1325\u001B[0m, in \u001B[0;36mIndexOpsMixin._arith_method\u001B[0;34m(self, other, op)\u001B[0m\n\u001B[1;32m   1322\u001B[0m rvalues \u001B[38;5;241m=\u001B[39m ensure_wrapped_if_datetimelike(rvalues)\n\u001B[1;32m   1324\u001B[0m \u001B[38;5;28;01mwith\u001B[39;00m np\u001B[38;5;241m.\u001B[39merrstate(\u001B[38;5;28mall\u001B[39m\u001B[38;5;241m=\u001B[39m\u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mignore\u001B[39m\u001B[38;5;124m\"\u001B[39m):\n\u001B[0;32m-> 1325\u001B[0m     result \u001B[38;5;241m=\u001B[39m \u001B[43mops\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43marithmetic_op\u001B[49m\u001B[43m(\u001B[49m\u001B[43mlvalues\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mrvalues\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mop\u001B[49m\u001B[43m)\u001B[49m\n\u001B[1;32m   1327\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_construct_result(result, name\u001B[38;5;241m=\u001B[39mres_name)\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/ops/array_ops.py:218\u001B[0m, in \u001B[0;36marithmetic_op\u001B[0;34m(left, right, op)\u001B[0m\n\u001B[1;32m    205\u001B[0m \u001B[38;5;66;03m# NB: We assume that extract_array and ensure_wrapped_if_datetimelike\u001B[39;00m\n\u001B[1;32m    206\u001B[0m \u001B[38;5;66;03m#  have already been called on `left` and `right`,\u001B[39;00m\n\u001B[1;32m    207\u001B[0m \u001B[38;5;66;03m#  and `maybe_prepare_scalar_for_op` has already been called on `right`\u001B[39;00m\n\u001B[1;32m    208\u001B[0m \u001B[38;5;66;03m# We need to special-case datetime64/timedelta64 dtypes (e.g. because numpy\u001B[39;00m\n\u001B[1;32m    209\u001B[0m \u001B[38;5;66;03m# casts integer dtypes to timedelta64 when operating with timedelta64 - GH#22390)\u001B[39;00m\n\u001B[1;32m    211\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m (\n\u001B[1;32m    212\u001B[0m     should_extension_dispatch(left, right)\n\u001B[1;32m    213\u001B[0m     \u001B[38;5;129;01mor\u001B[39;00m \u001B[38;5;28misinstance\u001B[39m(right, (Timedelta, BaseOffset, Timestamp))\n\u001B[0;32m   (...)\u001B[0m\n\u001B[1;32m    216\u001B[0m     \u001B[38;5;66;03m# Timedelta/Timestamp and other custom scalars are included in the check\u001B[39;00m\n\u001B[1;32m    217\u001B[0m     \u001B[38;5;66;03m# because numexpr will fail on it, see GH#31457\u001B[39;00m\n\u001B[0;32m--> 218\u001B[0m     res_values \u001B[38;5;241m=\u001B[39m \u001B[43mop\u001B[49m\u001B[43m(\u001B[49m\u001B[43mleft\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mright\u001B[49m\u001B[43m)\u001B[49m\n\u001B[1;32m    219\u001B[0m \u001B[38;5;28;01melse\u001B[39;00m:\n\u001B[1;32m    220\u001B[0m     \u001B[38;5;66;03m# TODO we should handle EAs consistently and move this check before the if/else\u001B[39;00m\n\u001B[1;32m    221\u001B[0m     \u001B[38;5;66;03m# (https://github.com/pandas-dev/pandas/issues/41165)\u001B[39;00m\n\u001B[1;32m    222\u001B[0m     _bool_arith_check(op, left, right)\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/arrays/datetimelike.py:2035\u001B[0m, in \u001B[0;36mTimelikeOps.__array_ufunc__\u001B[0;34m(self, ufunc, method, *inputs, **kwargs)\u001B[0m\n\u001B[1;32m   2027\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m (\n\u001B[1;32m   2028\u001B[0m     ufunc \u001B[38;5;129;01min\u001B[39;00m [np\u001B[38;5;241m.\u001B[39misnan, np\u001B[38;5;241m.\u001B[39misinf, np\u001B[38;5;241m.\u001B[39misfinite]\n\u001B[1;32m   2029\u001B[0m     \u001B[38;5;129;01mand\u001B[39;00m \u001B[38;5;28mlen\u001B[39m(inputs) \u001B[38;5;241m==\u001B[39m \u001B[38;5;241m1\u001B[39m\n\u001B[1;32m   2030\u001B[0m     \u001B[38;5;129;01mand\u001B[39;00m inputs[\u001B[38;5;241m0\u001B[39m] \u001B[38;5;129;01mis\u001B[39;00m \u001B[38;5;28mself\u001B[39m\n\u001B[1;32m   2031\u001B[0m ):\n\u001B[1;32m   2032\u001B[0m     \u001B[38;5;66;03m# numpy 1.18 changed isinf and isnan to not raise on dt64/td64\u001B[39;00m\n\u001B[1;32m   2033\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mgetattr\u001B[39m(ufunc, method)(\u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_ndarray, \u001B[38;5;241m*\u001B[39m\u001B[38;5;241m*\u001B[39mkwargs)\n\u001B[0;32m-> 2035\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28;43msuper\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m__array_ufunc__\u001B[49m\u001B[43m(\u001B[49m\u001B[43mufunc\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mmethod\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43minputs\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43mkwargs\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/arrays/base.py:1664\u001B[0m, in \u001B[0;36mExtensionArray.__array_ufunc__\u001B[0;34m(self, ufunc, method, *inputs, **kwargs)\u001B[0m\n\u001B[1;32m   1659\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28many\u001B[39m(\n\u001B[1;32m   1660\u001B[0m     \u001B[38;5;28misinstance\u001B[39m(other, (ABCSeries, ABCIndex, ABCDataFrame)) \u001B[38;5;28;01mfor\u001B[39;00m other \u001B[38;5;129;01min\u001B[39;00m inputs\n\u001B[1;32m   1661\u001B[0m ):\n\u001B[1;32m   1662\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mNotImplemented\u001B[39m\n\u001B[0;32m-> 1664\u001B[0m result \u001B[38;5;241m=\u001B[39m \u001B[43marraylike\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mmaybe_dispatch_ufunc_to_dunder_op\u001B[49m\u001B[43m(\u001B[49m\n\u001B[1;32m   1665\u001B[0m \u001B[43m    \u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mufunc\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mmethod\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43minputs\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43mkwargs\u001B[49m\n\u001B[1;32m   1666\u001B[0m \u001B[43m\u001B[49m\u001B[43m)\u001B[49m\n\u001B[1;32m   1667\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m result \u001B[38;5;129;01mis\u001B[39;00m \u001B[38;5;129;01mnot\u001B[39;00m \u001B[38;5;28mNotImplemented\u001B[39m:\n\u001B[1;32m   1668\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m result\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/_libs/ops_dispatch.pyx:113\u001B[0m, in \u001B[0;36mpandas._libs.ops_dispatch.maybe_dispatch_ufunc_to_dunder_op\u001B[0;34m()\u001B[0m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/arrays/datetimelike.py:1486\u001B[0m, in \u001B[0;36mDatetimeLikeArrayMixin.__radd__\u001B[0;34m(self, other)\u001B[0m\n\u001B[1;32m   1484\u001B[0m \u001B[38;5;28;01mdef\u001B[39;00m \u001B[38;5;21m__radd__\u001B[39m(\u001B[38;5;28mself\u001B[39m, other):\n\u001B[1;32m   1485\u001B[0m     \u001B[38;5;66;03m# alias for __add__\u001B[39;00m\n\u001B[0;32m-> 1486\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[38;5;21;43m__add__\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43mother\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/ops/common.py:72\u001B[0m, in \u001B[0;36m_unpack_zerodim_and_defer.<locals>.new_method\u001B[0;34m(self, other)\u001B[0m\n\u001B[1;32m     68\u001B[0m             \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mNotImplemented\u001B[39m\n\u001B[1;32m     70\u001B[0m other \u001B[38;5;241m=\u001B[39m item_from_zerodim(other)\n\u001B[0;32m---> 72\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[43mmethod\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mother\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/arrays/datetimelike.py:1460\u001B[0m, in \u001B[0;36mDatetimeLikeArrayMixin.__add__\u001B[0;34m(self, other)\u001B[0m\n\u001B[1;32m   1457\u001B[0m     result \u001B[38;5;241m=\u001B[39m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_add_timedelta_arraylike(other)\n\u001B[1;32m   1458\u001B[0m \u001B[38;5;28;01melif\u001B[39;00m is_object_dtype(other_dtype):\n\u001B[1;32m   1459\u001B[0m     \u001B[38;5;66;03m# e.g. Array/Index of DateOffset objects\u001B[39;00m\n\u001B[0;32m-> 1460\u001B[0m     result \u001B[38;5;241m=\u001B[39m \u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m_addsub_object_array\u001B[49m\u001B[43m(\u001B[49m\u001B[43mother\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43moperator\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43madd\u001B[49m\u001B[43m)\u001B[49m\n\u001B[1;32m   1461\u001B[0m \u001B[38;5;28;01melif\u001B[39;00m is_datetime64_dtype(other_dtype) \u001B[38;5;129;01mor\u001B[39;00m is_datetime64tz_dtype(other_dtype):\n\u001B[1;32m   1462\u001B[0m     \u001B[38;5;66;03m# DatetimeIndex, ndarray[datetime64]\u001B[39;00m\n\u001B[1;32m   1463\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_add_datetime_arraylike(other)\n",
      "File \u001B[0;32m~/PycharmProjects/pythonProject/.venv/lib/python3.10/site-packages/pandas/core/arrays/datetimelike.py:1385\u001B[0m, in \u001B[0;36mDatetimeLikeArrayMixin._addsub_object_array\u001B[0;34m(self, other, op)\u001B[0m\n\u001B[1;32m   1382\u001B[0m \u001B[38;5;28;01mwith\u001B[39;00m warnings\u001B[38;5;241m.\u001B[39mcatch_warnings():\n\u001B[1;32m   1383\u001B[0m     \u001B[38;5;66;03m# filter out warnings about Timestamp.freq\u001B[39;00m\n\u001B[1;32m   1384\u001B[0m     warnings\u001B[38;5;241m.\u001B[39mfilterwarnings(\u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mignore\u001B[39m\u001B[38;5;124m\"\u001B[39m, category\u001B[38;5;241m=\u001B[39m\u001B[38;5;167;01mFutureWarning\u001B[39;00m)\n\u001B[0;32m-> 1385\u001B[0m     res_values \u001B[38;5;241m=\u001B[39m \u001B[43mop\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mastype\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;124;43m\"\u001B[39;49m\u001B[38;5;124;43mO\u001B[39;49m\u001B[38;5;124;43m\"\u001B[39;49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mnp\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43masarray\u001B[49m\u001B[43m(\u001B[49m\u001B[43mother\u001B[49m\u001B[43m)\u001B[49m\u001B[43m)\u001B[49m\n\u001B[1;32m   1387\u001B[0m result \u001B[38;5;241m=\u001B[39m pd_array(res_values\u001B[38;5;241m.\u001B[39mravel())\n\u001B[1;32m   1388\u001B[0m result \u001B[38;5;241m=\u001B[39m extract_array(result, extract_numpy\u001B[38;5;241m=\u001B[39m\u001B[38;5;28;01mTrue\u001B[39;00m)\u001B[38;5;241m.\u001B[39mreshape(\u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mshape)\n",
      "\u001B[0;31mTypeError\u001B[0m: unsupported operand type(s) for +: 'NaTType' and 'str'"
     ]
    }
   ],
   "source": [
    "df.loc[df['age_class'].isnull(), 'age_class'] = df['sex']+df[df['net_time'].isnull()]['official_time']"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [
    "df.loc[(df['age'].loc[13524] > df['class_age'])]"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "outputs": [],
   "source": [
    "#treating the nulls in the net time. When net time is null, net_time = official_time\n",
    "#df.loc[df['age_class'].isnull(), 'age_class'] = df['sex']+df['age'].astype(str)\n",
    "#df.loc[[13524,43207,76596,110156,115456]]"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "outputs": [
    {
     "data": {
      "text/plain": "       place age_class place_in_class   bib                       name sex  \\\n13524   1317       NaN            285  1117                João Campos   M   \n43207    993       NaN            203  1889               Nuno Ribeiro   M   \n76569   1127       NaN            253  4149               Nuno Ribeiro   M   \n110156  4400       NaN            441  9019  Jose Manuel Ribeiro Lages   M   \n115456  4808       NaN           1464  7872              André  Ferraz   M   \n\n       nation          team   official_time        net_time birth_date  \\\n13524      PT    Individual 0 days 00:50:00 0 days 00:49:50 1975-12-20   \n43207      PT    Individual 0 days 03:54:14 0 days 03:53:49 1979-09-15   \n76569      PT    Individual 0 days 01:42:15 0 days 01:40:08 1979-09-15   \n110156     PT    Individual 0 days 01:06:49 0 days 01:04:52 1967-02-02   \n115456     PT  Bifanas Team 0 days 00:59:32 0 days 00:53:19 1985-01-31   \n\n                event  event_year distance class_gender class_age  age  \n13524      dia-do-pai        2015       10            n       NaN   40  \n43207        maratona        2012       42            n       NaN   33  \n76569   meia_maratona        2015       21            n       NaN   36  \n110156  sao-silvestre        2012       10            n       NaN   45  \n115456  sao-silvestre        2013       10            n       NaN   28  ",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>place</th>\n      <th>age_class</th>\n      <th>place_in_class</th>\n      <th>bib</th>\n      <th>name</th>\n      <th>sex</th>\n      <th>nation</th>\n      <th>team</th>\n      <th>official_time</th>\n      <th>net_time</th>\n      <th>birth_date</th>\n      <th>event</th>\n      <th>event_year</th>\n      <th>distance</th>\n      <th>class_gender</th>\n      <th>class_age</th>\n      <th>age</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>13524</th>\n      <td>1317</td>\n      <td>NaN</td>\n      <td>285</td>\n      <td>1117</td>\n      <td>João Campos</td>\n      <td>M</td>\n      <td>PT</td>\n      <td>Individual</td>\n      <td>0 days 00:50:00</td>\n      <td>0 days 00:49:50</td>\n      <td>1975-12-20</td>\n      <td>dia-do-pai</td>\n      <td>2015</td>\n      <td>10</td>\n      <td>n</td>\n      <td>NaN</td>\n      <td>40</td>\n    </tr>\n    <tr>\n      <th>43207</th>\n      <td>993</td>\n      <td>NaN</td>\n      <td>203</td>\n      <td>1889</td>\n      <td>Nuno Ribeiro</td>\n      <td>M</td>\n      <td>PT</td>\n      <td>Individual</td>\n      <td>0 days 03:54:14</td>\n      <td>0 days 03:53:49</td>\n      <td>1979-09-15</td>\n      <td>maratona</td>\n      <td>2012</td>\n      <td>42</td>\n      <td>n</td>\n      <td>NaN</td>\n      <td>33</td>\n    </tr>\n    <tr>\n      <th>76569</th>\n      <td>1127</td>\n      <td>NaN</td>\n      <td>253</td>\n      <td>4149</td>\n      <td>Nuno Ribeiro</td>\n      <td>M</td>\n      <td>PT</td>\n      <td>Individual</td>\n      <td>0 days 01:42:15</td>\n      <td>0 days 01:40:08</td>\n      <td>1979-09-15</td>\n      <td>meia_maratona</td>\n      <td>2015</td>\n      <td>21</td>\n      <td>n</td>\n      <td>NaN</td>\n      <td>36</td>\n    </tr>\n    <tr>\n      <th>110156</th>\n      <td>4400</td>\n      <td>NaN</td>\n      <td>441</td>\n      <td>9019</td>\n      <td>Jose Manuel Ribeiro Lages</td>\n      <td>M</td>\n      <td>PT</td>\n      <td>Individual</td>\n      <td>0 days 01:06:49</td>\n      <td>0 days 01:04:52</td>\n      <td>1967-02-02</td>\n      <td>sao-silvestre</td>\n      <td>2012</td>\n      <td>10</td>\n      <td>n</td>\n      <td>NaN</td>\n      <td>45</td>\n    </tr>\n    <tr>\n      <th>115456</th>\n      <td>4808</td>\n      <td>NaN</td>\n      <td>1464</td>\n      <td>7872</td>\n      <td>André  Ferraz</td>\n      <td>M</td>\n      <td>PT</td>\n      <td>Bifanas Team</td>\n      <td>0 days 00:59:32</td>\n      <td>0 days 00:53:19</td>\n      <td>1985-01-31</td>\n      <td>sao-silvestre</td>\n      <td>2013</td>\n      <td>10</td>\n      <td>n</td>\n      <td>NaN</td>\n      <td>28</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#removing man that run in a fem. class\n",
    "df = df.drop(index=df[(df['sex']=='M') & (df['class_gender']=='F')].index)\n",
    "#removing women that runned in a masc. class\n",
    "df = df.drop(index=df[(df['sex']=='F') & (df['class_gender']=='M')].index)\n",
    "#removing people ith no legal age to run more than 10km (less than 14 yo), this will also remove inconsistance like (born in the year of the event)\n",
    "df = df.drop(index=df[df['age']<14].index)\n",
    "#removing people without age_class\n",
    "df[df['age_class'].isnull()]"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Spliting our dataset"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "For each database we have, we will split in different dataset. This will help to select the data correctly, and allow the code to me more organized. We previously created the databases that did not have any foreing key, than, we merged then to the main df to split their foreing keys to the other tables.\n",
    "We need to assure that our merges does not duplicate the main table, creating more records than previous stated. So, we decided to perform a lef join with the left table being always (in this case) the main df."
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "outputs": [],
   "source": [
    "# Team: team name, team id.\n",
    "df_team = pd.DataFrame([])\n",
    "df_team['team'] = df['team'].unique()\n",
    "df_team.insert(0, 'id_team', range(0, 0 + len(df_team)))"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "outputs": [],
   "source": [
    "# Athlete: id, name, sex, nation, birth_date\n",
    "df_athlete = df[['name', 'sex','nation','birth_date']].drop_duplicates()\n",
    "df_athlete.insert(0, 'id_athlete', range(0, 0 + len(df_athlete)))"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "outputs": [],
   "source": [
    "# Events: event_id, event, event_year, distance\n",
    "df_events = df[['event', 'event_year', 'distance']].drop_duplicates()\n",
    "df_events.insert(0, 'id_event', range(0, 0 + len(df_events)))"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "outputs": [],
   "source": [
    "# populate id_athlete on df\n",
    "df = pd.merge(df,df_athlete[['name','birth_date','sex','nation','id_athlete']], how='left', on=['name','birth_date','sex','nation'])"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "outputs": [],
   "source": [
    "#populate id_team on df\n",
    "df = pd.merge(df,df_team[['team','id_team']], how='left', on=['team'])"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "outputs": [],
   "source": [
    "#populate id_event on df\n",
    "df = pd.merge(df,df_events[['event','event_year', 'distance','id_event']], how='left', on=['event', 'event_year', 'distance'])"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "outputs": [],
   "source": [
    "# Runner: id_runner, bib, age_class, id_event, id_athlete\n",
    "df_runner = df[['bib','age_class','id_athlete','id_event']].drop_duplicates()\n",
    "df_runner.insert(0, 'id_runner', range(0, 0 + len(df_runner)))"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "outputs": [],
   "source": [
    "# populate runner_id\n",
    "df = pd.merge(df,df_runner[['bib','age_class','id_athlete','id_event','id_runner']], how='left', on=['bib','age_class','id_athlete','id_event'])"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "outputs": [
    {
     "data": {
      "text/plain": "id_team      object\nid_runner    object\ndtype: object"
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_runner_team = df[['id_team','id_runner']].drop_duplicates()\n",
    "df_runner_team['id_team'] = df_runner_team['id_team'].astype(str)\n",
    "df_runner_team['id_runner'] = df_runner_team['id_runner'].astype(str)\n",
    "df_runner_team.dtypes"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "outputs": [],
   "source": [
    "# Event_ranking: id_event, id_runner, place, place_in_class, official_time, net_time\n",
    "df_ranking = df[['place','place_in_class', 'official_time', 'net_time','id_runner','id_event']].drop_duplicates()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Inserting in the Postgrees"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%% md\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "outputs": [],
   "source": [
    "#connecting with Postgrees\n",
    "con = psycopg2.connect(\n",
    "  database=\"fced_diogo_cruz\",             # your database is the same as your username\n",
    "  user=\"fced_diogo_cruz\",                 # your username\n",
    "  password=\"fced_diogo_cruz\",             # your password\n",
    "  host=\"dbm.fe.up.pt\",                    # the database host\n",
    "  options='-c search_path=schema_grupo5',\n",
    "  port=\"5433\"                            # use the schema you want to connect to\n",
    ")"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table dropped... \n"
     ]
    }
   ],
   "source": [
    " #Creating a cursor object using the cursor() method\n",
    "cursor = con.cursor()\n",
    "cursor.execute(\"TRUNCATE events CASCADE\")\n",
    "print(\"Table dropped... \")\n",
    "#Commit your changes in the database\n",
    "con.commit()\n",
    "#Closing the connection\n",
    "con.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "INSERT INTO events(id_event,event,event_year,distance) VALUES %s\n",
      "the dataframe is inserted\n"
     ]
    }
   ],
   "source": [
    "#events\n",
    "cur = con.cursor()\n",
    "table=\"events\"\n",
    "cols = ','.join(list(df_events.columns))\n",
    "query = \"INSERT INTO %s(%s) VALUES %%s\" % (table, cols)\n",
    "tuples = [tuple(x) for x in df_events.to_numpy()]\n",
    "\n",
    "try:\n",
    "\n",
    "    extras.execute_values(cur, query, tuples)\n",
    "    con.commit()\n",
    "    print(\"the dataframe is inserted\")\n",
    "except (Exception, psycopg2.DatabaseError) as error:\n",
    "    print(\"Error: %s\" % error)\n",
    "    con.rollback()\n",
    "    cur.close()\n",
    "cur.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the dataframe is inserted\n"
     ]
    }
   ],
   "source": [
    "#athlete\n",
    "cur = con.cursor()\n",
    "table=\"athlete\"\n",
    "cols = ','.join(list(df_athlete.columns))\n",
    "query = \"INSERT INTO %s(%s) VALUES %%s\" % (table, cols)\n",
    "tuples = [tuple(x) for x in df_athlete.to_numpy()]\n",
    "\n",
    "try:\n",
    "\n",
    "    extras.execute_values(cur, query, tuples)\n",
    "    con.commit()\n",
    "    print(\"the dataframe is inserted\")\n",
    "except (Exception, psycopg2.DatabaseError) as error:\n",
    "    print(\"Error: %s\" % error)\n",
    "    con.rollback()\n",
    "    cur.close()\n",
    "cur.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the dataframe is inserted\n"
     ]
    }
   ],
   "source": [
    "#team\n",
    "cur = con.cursor()\n",
    "table=\"teams\"\n",
    "cols = ','.join(list(df_team.columns))\n",
    "query = \"INSERT INTO %s(%s) VALUES %%s\" % (table, cols)\n",
    "tuples = [tuple(x) for x in df_team.to_numpy()]\n",
    "\n",
    "try:\n",
    "\n",
    "    extras.execute_values(cur, query, tuples)\n",
    "    con.commit()\n",
    "    print(\"the dataframe is inserted\")\n",
    "except (Exception, psycopg2.DatabaseError) as error:\n",
    "    print(\"Error: %s\" % error)\n",
    "    con.rollback()\n",
    "    cur.close()\n",
    "cur.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the dataframe is inserted\n"
     ]
    }
   ],
   "source": [
    "#runner\n",
    "cur = con.cursor()\n",
    "table=\"runner\"\n",
    "cols = ','.join(list(df_runner.columns))\n",
    "query = \"INSERT INTO %s(%s) VALUES %%s\" % (table, cols)\n",
    "tuples = [tuple(x) for x in df_runner.to_numpy()]\n",
    "\n",
    "try:\n",
    "    extras.execute_values(cur, query, tuples)\n",
    "    con.commit()\n",
    "    print(\"the dataframe is inserted\")\n",
    "except (Exception, psycopg2.DatabaseError) as error:\n",
    "    print(\"Error: %s\" % error)\n",
    "    con.rollback()\n",
    "    cur.close()\n",
    "cur.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the dataframe is inserted\n"
     ]
    }
   ],
   "source": [
    "#runner_team\n",
    "cur = con.cursor()\n",
    "table=\"runner_teams\"\n",
    "cols = ','.join(list(df_runner_team.columns))\n",
    "query = \"INSERT INTO %s(%s) VALUES %%s\" % (table, cols)\n",
    "tuples = [tuple(x) for x in df_runner_team.to_numpy()]\n",
    "\n",
    "try:\n",
    "    extras.execute_values(cur, query, tuples)\n",
    "    con.commit()\n",
    "    print(\"the dataframe is inserted\")\n",
    "except (Exception, psycopg2.DatabaseError) as error:\n",
    "    print(\"Error: %s\" % error)\n",
    "    con.rollback()\n",
    "    cur.close()\n",
    "cur.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the dataframe is inserted\n"
     ]
    }
   ],
   "source": [
    "#event_ranking\n",
    "cur = con.cursor()\n",
    "table=\"event_ranking\"\n",
    "cols = ','.join(list(df_ranking.columns))\n",
    "query = \"INSERT INTO %s(%s) VALUES %%s\" % (table, cols)\n",
    "tuples = [tuple(x) for x in df_ranking.to_numpy()]\n",
    "\n",
    "try:\n",
    "    extras.execute_values(cur, query, tuples)\n",
    "    con.commit()\n",
    "    print(\"the dataframe is inserted\")\n",
    "except (Exception, psycopg2.DatabaseError) as error:\n",
    "    print(\"Error: %s\" % error)\n",
    "    con.rollback()\n",
    "    cur.close()\n",
    "cur.close()"
   ],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false,
    "pycharm": {
     "name": "#%%\n"
    }
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}