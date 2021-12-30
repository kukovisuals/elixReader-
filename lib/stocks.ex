defmodule Stocks do
  @moduledoc """
 
      iex> Stocks.hello()
      :world

  """
  def hello do
    File.stream!("symbols.csv")
    |> CSV.decode(headers: true)
    |> Enum.take(8000)
  end
end
